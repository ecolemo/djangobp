from django.core.management.base import BaseCommand
from djangobp.editsettings import install_app

class Command(BaseCommand):
    args = 'app_name'
    help = 'installapp app_name'

    def handle(self, *args, **options):
        install_app(args[0])

            
