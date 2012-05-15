from django.core.management.base import BaseCommand
import importlib
import os
import shutil
import djangobp

class Command(BaseCommand):
    args = 'app'
    help = 'fill boilerplate codes for quick start'

    def handle(self, *args, **options):
        app_name = args[0]
        module = importlib.import_module(app_name)
        path = os.path.dirname(module.__file__) + os.sep
        
        shutil.copytree(os.path.dirname(djangobp.__file__) + os.sep + 'scaffold/app/controllers', path + 'controllers')
        shutil.copytree(os.path.dirname(djangobp.__file__) + os.sep + 'scaffold/app/templates', path + '/templates')
        shutil.copytree(os.path.dirname(djangobp.__file__) + os.sep + 'scaffold/app/static', path + '/static')
        
        # TODO urls.py edit: urlpatterns += (controller_method_resource_pattern, route(controller))
        # TODO settings.py edit: app

