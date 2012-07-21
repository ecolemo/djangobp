from django.conf import settings
from django.core.management.base import BaseCommand
from djangobp.editsettings import CodeEditor
import MySQLdb
import os

class Command(BaseCommand):
    args = 'database_name user password --superuser=superuser'
    help = '''create database named database_name using user and password. 
if superuser is specified, this command will be executed by superuser.'''

    def handle(self, *args, **options):
        database = args[0]
        user = args[1]
        password = args[2]
#        if 'superuser' in options: user = options['superuser']

        db = MySQLdb.connect(user=user, passwd=password)
        cursor = db.cursor()
        print 'CREATE SCHEMA `%s` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci' % database
        cursor.execute('CREATE SCHEMA `%s` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci' % database)
        cursor.close()
        db.close()
        print 'database %s created.' % database

        project_path = os.path.dirname(os.path.normpath(os.sys.modules[settings.SETTINGS_MODULE].__file__))
        edit = CodeEditor(project_path + os.sep + 'settings.py')
        edit.go_line('DATABASES = {')
        edit.go_line("'default': {")
        edit.replace_line("'ENGINE': 'django.db.backends.'", "'ENGINE': 'django.db.backends.mysql'")
        edit.replace_line("'NAME': ''", "'NAME': '%s'" % database)
        edit.replace_line("'USER': ''", "'USER': '%s'" % user)
        edit.replace_line("'PASSWORD': ''", "'PASSWORD': '%s'" % password)
        edit.commit()
        
        print "edited settings.py"