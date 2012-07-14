from djangobp.editsettings import CodeEditor
import unittest
from StringIO import StringIO

class TestEditSettings(unittest.TestCase):
    def test_edit(self):
        source = '''
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangobp',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)'''

        expected = '''
INSTALLED_APPS = (
    'sampleapp',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangobp',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)'''

        editor = CodeEditor(source)
        editor.insert_tuple_element('INSTALLED_APPS', 'sampleapp')
        self.assertEqual(expected, editor.to_source())
        