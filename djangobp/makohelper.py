from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse, HttpResponseServerError
from django.utils.importlib import import_module
from mako.lookup import TemplateLookup
from mako.template import Template
from mako import exceptions
import os
import sys

app_template_dirs = []
fs_encoding = sys.getfilesystemencoding() or sys.getdefaultencoding()

for app in settings.INSTALLED_APPS:
    try:
        mod = import_module(app)
    except ImportError, e:
        raise ImproperlyConfigured('ImportError %s: %s' % (app, e.args[0]))
    template_dir = os.path.join(os.path.dirname(mod.__file__), 'templates')
    if os.path.isdir(template_dir):
        app_template_dirs.append(template_dir.decode(fs_encoding))

template_lookup = TemplateLookup(directories=app_template_dirs, input_encoding='utf8', output_encoding='utf8', imports=['from djangobp.textutil import gettext as _'])
def render_to_response(filename, dictionary, context_instance=None):

    if context_instance:
        for context_dict in context_instance.dicts:
            dictionary.update(context_dict)
    try:
        template = template_lookup.get_template(filename)
        return HttpResponse(template.render(**dictionary))
    except:
        return HttpResponseServerError(exceptions.html_error_template().render())
    