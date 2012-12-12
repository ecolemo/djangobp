from distutils.file_util import copy_file
from django.core.management.base import BaseCommand
from djangobp.editsettings import install_app, CodeEditor
from django.conf import settings
import djangobp
import importlib
import os
from distutils.dir_util import copy_tree

class Command(BaseCommand):
    args = 'app'
    help = 'install django-social-auth'

    def handle(self, *args, **options):
        app_name = args[0]
        module = importlib.import_module(app_name)
        path = os.path.dirname(module.__file__) + os.sep
        
        project_path = os.path.dirname(os.path.normpath(os.sys.modules[settings.SETTINGS_MODULE].__file__))
        
        install_app('social_auth')

        copy_tree(os.path.dirname(djangobp.__file__) + os.sep + 'scaffold/socialauth/templates/accounts', path + '/templates/accounts', update=True)

        copy_file(os.path.dirname(djangobp.__file__) + os.sep + 'scaffold/socialauth/controllers/accounts.py', path + '/controllers', update=True)
        copy_file(os.path.dirname(djangobp.__file__) + os.sep + 'scaffold/scaffold/socialauthsettings.py', project_path, update=True)

        urls_edit = CodeEditor(path + 'urls.py')
        urls_edit.insert_line("url(r'', include('social_auth.urls')),", 'urlpatterns')
        urls_edit.commit()

        settings_edit = CodeEditor(project_path + os.sep + 'settings.py')
        settings_edit.append_line("from socialauthsettings import *")
        settings_edit.commit()
        
        # TODO copy controllers/accounts.py
        # TODO copy templates/accounts/login.html
        # TODO urls social auth
        # TODO django-social-auth settings
        
        