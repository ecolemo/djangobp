from django.http import HttpResponse, HttpResponseServerError
from django.utils import importlib
from django.utils.functional import curry
from mako import exceptions
from mako.lookup import TemplateLookup
from mako.template import Template
import datetime
import os
import simplejson
import sys
import pkgutil
import types
import inspect
from django.conf.urls import include, url

controller_resource_method_pattern = r'(?P<controller>[^/\?\&.]+)?(/(?P<resource_id>[^/\?\&.]+))?(/(?P<method>[^/\?\&.]+))?(?P<format>\.(\w+)$)?'

def router(controllers_root):
    return curry(route, controllers_root)

def route(controllers_root, request, controller=None, resource_id=None, method=None, format=None):
    request.format = format[1:] if format is not None else 'plain'

    request.app_name = controllers_root.__name__[:controllers_root.__name__.rfind('.')]
    if controller:
        module_name = controllers_root.__name__ + '.' + controller
    else:
        module_name = controllers_root.__name__
    
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

def discover_controllers(package):
    urls = []
    __import__(package)

    if hasattr(sys.modules[package], 'index'):
        urls.append(url('^$', getattr(sys.modules[package], 'index')))
    
    for _, name, _ in pkgutil.iter_modules([sys.modules[package].__path__[0]]):
        __import__(package + '.' + name)
        
        controller = sys.modules[package + '.' + name]
        
        for member in dir(controller):
            func = getattr(controller, member)
            if not inspect.isfunction(func): continue
            args = inspect.getargspec(func).args
            
            if len(args) == 0 or args[0] != 'request': continue
            
            urls.append(url(name + '/(?P<resource_id>[^/\?\&.]+)/' + member + '/?$', func))
            urls.append(url(name + '/' + member + '/?$', func))

        if 'show' in dir(controller):
            urls.append(url(name + '/(?P<resource_id>[^/\?\&.]+)/?$', getattr(controller, 'show')))
        if 'index' in dir(controller):
            urls.append(url(name + '$', getattr(controller, 'index')))
            
                
    return include(urls)
    
def render_to_response(filename, dictionary):
    # using app_name that is set by route()
    app_name = dictionary['request'].app_name
    templates = importlib.import_module(app_name + '.templates')

    try:
        template_lookup = TemplateLookup(directories=[templates.__path__[0]], input_encoding='utf8')
        template = Template(filename=templates.__path__[0] + os.sep + filename, input_encoding='utf8', output_encoding='utf8', template_lookup=template_lookup, imports=['from djangobp.textutil import gettext as _'])
        return HttpResponse(template.render(**dictionary))
    except:
        return HttpResponseServerError(exceptions.html_error_template().render())

@DeprecationWarning
class HttpResponseJSON(HttpResponse):
    def __init__(self, data):
        HttpResponse.__init__(self, simplejson.dumps(data, ensure_ascii=False, cls=JSONDateEncoder), content_type='application/json')

class JSONDateEncoder(simplejson.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat() + 'Z'
#            return obj.strftime('%Y-%m-%dT%H:%M:%S')
        else:
            return simplejson.JSONEncoder.default(self, obj)
        
def render_to_json(data):
    return HttpResponseJSON(data)

