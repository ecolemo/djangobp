import unittest
from djangobp.tests.controllers import sample, example
from django.core import urlresolvers

class MockRequest:
    def __init__(self,app_name='',format='plain'):
        self.app_name=app_name
        self.format = format
    def __eq__(self, other):
        return self.app_name == other.app_name and self.format == other.format

    def __repr__(self):
        return "%s:%s" % (self.app_name,self.format)

class RouteTest(unittest.TestCase):
    def test_route_depth_url(self):
        urlconf = 'tests.urls'
        urlresolvers.set_urlconf(urlconf)
        resolver = urlresolvers.RegexURLResolver(r'^/', urlconf)
        
        callback, args, kargs = resolver.resolve('/sample')
        request = MockRequest()
        self.assertEquals(sample.index(request, None), callback(request, *args, **kargs))

        callback, args, kargs = resolver.resolve('/sample/5')
        self.assertEquals(sample.show(request, '5'), callback(request, *args, **kargs))

        callback, args, kargs = resolver.resolve('/sample/5.xml')
        requestXML = MockRequest(app_name='djangobp.tests', format='xml')
        self.assertEquals(sample.show(requestXML, '5'), callback(request, *args, **kargs))

        callback, args, kargs = resolver.resolve('/sample/5.json')
        requestXML = MockRequest(app_name='djangobp.tests', format='json')
        self.assertEquals(sample.show(requestXML, '5'), callback(request, *args, **kargs))

        callback, args, kargs = resolver.resolve('/sample/ok/edit')
        self.assertEquals(sample.edit(request, 'ok'), callback(request, *args, **kargs))

        callback, args, kargs = resolver.resolve('/example/hello/test')
        self.assertEquals(example.test(request, 'hello'), callback(request, *args, **kargs))

        callback, args, kargs = resolver.resolve('/example/pick')
        self.assertEquals(example.pick(request, None), callback(request, *args, **kargs))

        callback, args, kargs = resolver.resolve('/example/nopick')
        self.assertEquals(example.show(request, 'nopick'), callback(request, *args, **kargs))
