from django.http import HttpResponse, HttpResponseServerError
from mako.lookup import TemplateLookup
from mako.template import Template
import os
from mako import exceptions
from django.utils import importlib
from django.template import loader

def render_to_response(filename, dictionary):
    app_name = dictionary['request'].app_name
    
    templates = importlib.import_module(app_name + '.templates')
    try:
        print templates.__path__[0]
        lookup = TemplateLookup(directories=[templates.__path__[0]], input_encoding='utf8')
        template = Template(filename=templates.__path__[0] + os.sep + filename, input_encoding='utf8', output_encoding='utf8', lookup=lookup)
        return HttpResponse(template.render(**dictionary))
    except:
        return HttpResponseServerError(exceptions.html_error_template().render())


class MakoMiddleware():
    def __init__(self):
        self.app_name = None
        
    def process_view(self, request, view_func, view_args, view_kwargs):
        if not self.app_name:
            self.app_name = '.'.join(view_func.__module__.split('.')[0:-2])
        request.app_name = self.app_name
        