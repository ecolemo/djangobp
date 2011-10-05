# coding: utf8
from django.core.management import execute_manager
import os
import sys

class Fixture(object):
    def __init__(self, settings):
        self.settings = settings
        path = os.path.dirname(settings.__file__)
        sys.path.insert(0, path)
        os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

    def reset(self, app_name):
        execute_manager(self.settings, ['', 'reset', app_name, '--noinput'])

    def load_json(self, name):
        pass
#        execute_manager(self.settings, ['', 'loaddata', '%s/pytmon/spec/fixtures/%s.json' % (path, name)])