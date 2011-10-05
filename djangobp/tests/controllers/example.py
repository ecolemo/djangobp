from inspect import stack
def test(request, id):
    return __name__.split('.')[-1], stack()[0][3], request, id

def show(request, id):
    return __name__.split('.')[-1], stack()[0][3], request, id

def pick(request, id):
    return __name__.split('.')[-1], stack()[0][3], request, id
