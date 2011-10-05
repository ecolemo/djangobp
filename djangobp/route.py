import sys
from django.utils.functional import curry

controller_resource_method_pattern = r'(?P<controller>[^/\?\&]+)(/(?P<resource_id>[^/\?\&]+))?(/(?P<method>[^/\?\&]+))?'

def router(controllers_root):
    return curry(route, controllers_root)

def route(controllers_root, request, controller='root', resource_id=None, method=None):
    request.app_name = controllers_root.__name__[:controllers_root.__name__.rfind('.')]
    module_name = controllers_root.__name__ + '.' + controller
    __import__(module_name)

    if not method:
        if resource_id: 
            if hasattr(sys.modules[module_name], resource_id):
                method = resource_id
                resource_id = None
            else:
                method = 'show'
        else: method = 'index'
        
    return getattr(sys.modules[module_name], method)(request, resource_id)
