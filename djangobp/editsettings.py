from django.conf import settings
import importlib
import os
import re

def install_app(app_name):
    try:
        importlib.import_module(app_name)
    except:
        print 'cannot import %s' % app_name
        return
    
    project_path = os.path.dirname(os.path.normpath(os.sys.modules[settings.SETTINGS_MODULE].__file__))
    settings_edit = CodeEditor(project_path + os.sep + 'settings.py')
    settings_edit.insert_line("    '%s'," % app_name, 'INSTALLED_APPS')
    settings_edit.commit()
    print "edited " + project_path + os.sep + 'settings.py'
        
class CodeEditor(object):
    
    def __init__(self, filename):
        self.filename = filename
        source = open(filename, 'r').read()
        self.lines = source.splitlines()
        self.cursor = 0

    def insert_tuple_element(self, name, value):
        for index, line in enumerate(self.lines):
            if line.strip().startswith(name):
                insert_index = index + 1
                break
        
        self.lines.insert(insert_index, '    ' + repr(value) + ',')

    def go_line(self, expr):
        for index, l in enumerate(self.lines[self.cursor:], self.cursor):
            if expr in l:
                self.cursor = index
                break
    
    def replace_all(self, expr, replacement):
        for index, l in enumerate(self.lines, self.cursor):
            if expr in l:
                self.lines[index] = l.replace(expr, replacement)
                
    def replace_line(self, expr, replacement):
        for index, l in enumerate(self.lines[self.cursor:], self.cursor):
            if expr in l:
                self.cursor = index
                break
            
        self.lines[self.cursor] = self.lines[self.cursor].replace(expr, replacement)
        
    def insert_line(self, line, after):
        if line in self.lines: return
        
        insert_index = 0
        for index, l in enumerate(self.lines[self.cursor:], self.cursor):
            if re.match(after, l):
                insert_index = index + 1
                break;
        self.lines.insert(insert_index, line)

    def append_line(self, line):
        self.lines.append(line)
        
    def to_source(self):
        return '\n'.join(self.lines)
    
    def commit(self):
        open(self.filename, 'w').write(self.to_source())