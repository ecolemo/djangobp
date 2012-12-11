from social_auth.context_processors import social_auth_by_type_backends
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from djangobp.makohelper import render_to_response
from django.template.defaulttags import csrf_token
from django.template.base import Template
from django.template.context import RequestContext

def login(request):
    reverse_url = reverse
    l = locals()
    l.update(social_auth_by_type_backends(request))
    return render_to_response('accounts/login.html', l, RequestContext(request))

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')
