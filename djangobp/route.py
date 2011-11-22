from django.http import HttpResponse, HttpResponseServerError
from django.utils import importlib
from django.utils.functional import curry
from mako import exceptions
from mako.lookup import TemplateLookup
from mako.template import Template
import os
import sys

controller_resource_method_pattern = r'(?P<controller>[^/\?\&]+)(/(?P<resource_id>[^/\?\&]+))?(/(?P<method>[^/\?\&]+))?'

def router(controllers_root):
    return curry(route, controllers_root)

def route(controllers_root, request, controller='root', resource_id=None, method=None):
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
        
    return getattr(sys.modules[module_name], method)(request, resource_id)


def render_to_response(filename, dictionary):
    # using app_name that is set by route()
    app_name = dictionary['request'].app_name
    templates = importlib.import_module(app_name + '.templates')
    try:
        lookup = TemplateLookup(directories=[templates.__path__[0]], input_encoding='utf8')
        template = Template(filename=templates.__path__[0] + os.sep + filename, input_encoding='utf8', output_encoding='utf8', lookup=lookup)
        return HttpResponse(template.render(**dictionary))
    except:
        return HttpResponseServerError(exceptions.html_error_template().render())
        