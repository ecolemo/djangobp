from djangobp.route import render_to_response
from social_auth.context_processors import social_auth_by_type_backends
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def login(request):
    csrf_token = csrf(request)['csrf_token']
    reverse_url = reverse
    l = locals()
    l.update(social_auth_by_type_backends(request))
    return render_to_response('login.html', l)

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/issues')
