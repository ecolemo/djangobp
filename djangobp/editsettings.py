import re
class CodeEditor(object):
    
    def __init__(self, filename):
        self.filename = filename
        source = open(filename, 'r').read()
        self.lines = source.splitlines()

    def insert_tuple_element(self, name, value):
        for index, line in enumerate(self.lines):
            if line.strip().startswith(name):
                insert_index = index + 1
                break
        
        self.lines.insert(insert_index, '    ' + repr(value) + ',')

    def insert_line(self, line, after):
        insert_index = 0
        for index, l in enumerate(self.lines):
            if re.match(after, l):
                insert_index = index + 1
                break;
        self.lines.insert(insert_index, line)
        
    def to_source(self):
        return '\n'.join(self.lines)
    
    def commit(self):
        open(self.filename, 'w').write(self.to_source())