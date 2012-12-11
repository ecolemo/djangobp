from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from djangobp.makohelper import render_to_response

@login_required
def index(request):
    return render_to_response('useract.html', locals())