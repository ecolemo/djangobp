import os
import sys
import settings
path = os.path.dirname(settings.__file__) + '/..'
sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'