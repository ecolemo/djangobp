from django.conf.urls import patterns, include, url
from djangobp.route import discover_controllers

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
    (r'', discover_controllers('socialauth.controllers')),
)
