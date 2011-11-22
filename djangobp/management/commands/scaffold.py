from django.core.management.base import BaseCommand
import importlib

class Command(BaseCommand):
    args = 'app model'
    help = 'scaffold controller and views for specified model'

    def handle(self, *args, **options):
        model = importlib.import_module(args[1], args[0] + '.models')
        print model.__name__
