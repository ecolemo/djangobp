from djangobp.makohelper import render_to_response

def index(request):
    return render_to_response('index.html', locals())