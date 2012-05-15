from djangobp.route import render_to_response

def index(request, resource_id):
    return render_to_response('index.html', locals())