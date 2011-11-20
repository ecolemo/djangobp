from django.http import HttpResponse, HttpResponseServerError
from django.utils import importlib
from django.utils.functional import curry
from mako import exceptions
from mako.lookup import TemplateLookup
from mako.template import Template
import os
import sys
import simplejson

controller_resource_method_pattern = r'(?P<controller>[^/\?\&]+)(/(?P<resource_id>[^/\?\&]+))?(/(?P<method>[^/\?\&]+))?'

def router(controllers_root):
    return curry(route, controllers_root)

def route(controllers_root, request, controller='root', resource_id=None, method=None):
    xml = False
    if controller.endswith('.xml'):
        xml = True
        controller = controller.replace('.xml','')

    if resource_id is not None and resource_id.endswith('.xml'):
        xml = True
        resource_id = resource_id.replace('.xml', '')

    request.app_name = controllers_root.__name__[:controllers_root.__name__.rfind('.')]
    module_name = controllers_root.__name__ + '.' + controller
    __import__(module_name)

    if not method:
        if resource_id: 
            if hasattr(sys.modules[module_name], resource_id):
                method = resource_id
                resource_id = None
            else:
                method = 'show'
        else: method = 'index'
        if xml: method += '_xml'
        
    return getattr(sys.modules[module_name], method)(request, resource_id)


def render_to_response(filename, dictionary):
    # using app_name that is set by route()
    app_name = dictionary['request'].app_name
    print app_name
    templates = importlib.import_module(app_name + '.templates')
    try:
        print templates.__path__[0]
        lookup = TemplateLookup(directories=[templates.__path__[0]], input_encoding='utf8')
        template = Template(filename=templates.__path__[0] + os.sep + filename, input_encoding='utf8', output_encoding='utf8', lookup=lookup)
        return HttpResponse(template.render(**dictionary))
    except:
        return HttpResponseServerError(exceptions.html_error_template().render())

class HttpResponseJSON(HttpResponse):
    def __init__(self, data):
        HttpResponse.__init__(self, simplejson.dumps(data, ensure_ascii=False), content_type='application/json')

def render_to_json(data):
    return HttpResponseJSON(data)

