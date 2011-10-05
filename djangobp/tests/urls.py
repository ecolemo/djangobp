from django.conf.urls.defaults import patterns
from djangobp.tests import controllers
from djangobp.route import controller_resource_method_pattern, router

urlpatterns = patterns('',
    (controller_resource_method_pattern, router(controllers)),
)