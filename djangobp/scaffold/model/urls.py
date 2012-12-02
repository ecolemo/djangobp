from django.conf.urls import patterns, include, url
from djangobp.route import discover_controllers

urlpatterns = patterns('',
    (r'', discover_controllers('model.controllers')),
)
