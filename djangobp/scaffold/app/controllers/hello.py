from djangobp.makohelper import render_to_response

def index(request):
    method = 'index'
    resource_id = None
    return render_to_response('hello.html', locals())

def show(request, resource_id):
    method = 'show'
    return render_to_response('hello.html', locals())

def custom(request, resource_id):
    method = 'custom'
    return render_to_response('hello.html', locals())
    