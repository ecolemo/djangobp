from django.core.management.base import BaseCommand
import importlib
import os
import djangobp
from distutils.dir_util import copy_tree
from distutils.file_util import copy_file
from djangobp.editsettings import CodeEditor

class Command(BaseCommand):
    args = 'app'
    help = 'fill boilerplate codes for quick start'

    def handle(self, *args, **options):
        app_name = args[0]
        module = importlib.import_module(app_name)
        path = os.path.dirname(module.__file__) + os.sep
        
        copy_tree(os.path.dirname(djangobp.__file__) + os.sep + 'scaffold/app/controllers', path + 'controllers')
        copy_tree(os.path.dirname(djangobp.__file__) + os.sep + 'scaffold/app/templates', path + '/templates')
        copy_tree(os.path.dirname(djangobp.__file__) + os.sep + 'scaffold/app/static', path + '/static')
        
        copy_file(os.path.dirname(djangobp.__file__) + os.sep + 'scaffold/app/urls.py', path)
        
        urls_edit = CodeEditor(path + 'urls.py')
        urls_edit.insert_line("    (r'', discover_controllers('%s'))," % (app_name + '.controllers'), after='urlpatterns')
        urls_edit.commit()
        
#        main_urls_edit = CodeEditor(path + 'urls.py')
        
        # TODO urls.py edit: urlpatterns += (controller_method_resource_pattern, route(controller))
        # TODO settings.py edit: app

        