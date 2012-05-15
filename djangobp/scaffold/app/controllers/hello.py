from djangobp.route import render_to_response

def index(request, resource_id):
    method = 'index'
    return render_to_response('hello.html', locals())

def show(request, resource_id):
    method = 'show'
    return render_to_response('hello.html', locals())

def custom(request, resource_id):
    method = 'custom'
    return render_to_response('hello.html', locals())
    