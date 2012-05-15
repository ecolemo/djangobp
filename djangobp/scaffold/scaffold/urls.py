from django.conf.urls import patterns, include, url
from djangobp.route import controller_resource_method_pattern, router
import app.controllers

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (controller_resource_method_pattern, router(app.controllers)),
                   
    # Examples:
    # url(r'^$', 'scaffold.views.home', name='home'),
    # url(r'^scaffold/', include('scaffold.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
