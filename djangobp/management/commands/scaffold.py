from django.core.management.base import BaseCommand
import importlib
import os
from distutils.dir_util import copy_tree
import djangobp
from distutils.file_util import copy_file
from djangobp.editsettings import CodeEditor

class Command(BaseCommand):
    args = 'modelclass'
    help = 'scaffold controller and views for specified model'

    def handle(self, *args, **options):
        app_name = args[0].split('.')[0]
        module = importlib.import_module(app_name)
        path = os.path.dirname(module.__file__) + os.sep
        model_class = get_class(args[0])
        controller = model_class.__name__.lower()

        copy_tree(os.path.dirname(djangobp.__file__) + os.sep + 'scaffold/model/templates/sample', path + '/templates/' + controller , update=True)
        copy_tree(os.path.dirname(djangobp.__file__) + os.sep + 'scaffold/model/templates/common', path + '/templates/common', update=True)
        copy_file(os.path.dirname(djangobp.__file__) + os.sep + 'scaffold/model/controllers/sample.py', path + '/controllers/' + controller + '.py', update=True)

        controller_edit = CodeEditor(path + '/controllers/' + controller + '.py')
        controller_edit.replace_all('from djangobp.scaffold.model.models import Sample', 'from %s import %s' % (model_class.__module__, model_class.__name__))
        controller_edit.replace_all('Sample',  model_class.__name__)
        controller_edit.commit()

def get_class( kls ):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)            
    return m