from django.core.management.base import BaseCommand
import importlib
import os
import djangobp
from distutils.dir_util import copy_tree
from distutils.file_util import copy_file
from djangobp.editsettings import CodeEditor
from django.conf import settings

class Command(BaseCommand):
    args = 'app'
    help = 'fill boilerplate codes for quick start'

    def handle(self, *args, **options):
        app_name = args[0]
        module = importlib.import_module(app_name)
        path = os.path.dirname(module.__file__) + os.sep
        
        copy_tree(os.path.dirname(djangobp.__file__) + os.sep + 'scaffold/app/controllers', path + 'controllers', update=True)
        copy_tree(os.path.dirname(djangobp.__file__) + os.sep + 'scaffold/app/templates', path + '/templates', update=True)
        copy_tree(os.path.dirname(djangobp.__file__) + os.sep + 'scaffold/app/static', path + '/static', update=True)
        
        copy_file(os.path.dirname(djangobp.__file__) + os.sep + 'scaffold/app/urls.py', path, update=True)
        
        urls_edit = CodeEditor(path + 'urls.py')
        urls_edit.replace_all('app', app_name)
        urls_edit.commit()
        project_path = os.path.dirname(os.path.normpath(os.sys.modules[settings.SETTINGS_MODULE].__file__))
        main_urls_edit = CodeEditor(project_path + os.sep + 'urls.py')
        main_urls_edit.insert_line("    (r'', include('%s'))," % (app_name + '.urls'), after='urlpatterns')
        main_urls_edit.commit()
        
        settings_edit = CodeEditor(project_path + os.sep + 'settings.py')
        settings_edit.insert_line("    '%s'," % app_name, 'INSTALLED_APPS')
        settings_edit.commit()
        # TODO urls.py edit: urlpatterns += (controller_method_resource_pattern, route(controller))
        # TODO settings.py edit: app

        