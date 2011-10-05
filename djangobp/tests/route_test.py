import unittest
from djangobp.tests.controllers import sample, example
from django.core import urlresolvers

class RouteTest(unittest.TestCase):
    def test_route_depth_url(self):
        urlconf = 'tests.urls'
        urlresolvers.set_urlconf(urlconf)
        resolver = urlresolvers.RegexURLResolver(r'^/', urlconf)
        
        callback, args, kargs = resolver.resolve('/sample')
        self.assertEquals(sample.index('request', None), callback('request', *args, **kargs))

        callback, args, kargs = resolver.resolve('/sample/5')
        self.assertEquals(sample.show('request', '5'), callback('request', *args, **kargs))

        callback, args, kargs = resolver.resolve('/sample/ok/edit')
        self.assertEquals(sample.edit('request', 'ok'), callback('request', *args, **kargs))

        callback, args, kargs = resolver.resolve('/example/hello/test')
        self.assertEquals(example.test('request', 'hello'), callback('request', *args, **kargs))

        callback, args, kargs = resolver.resolve('/example/pick')
        self.assertEquals(example.pick('request', None), callback('request', *args, **kargs))

        callback, args, kargs = resolver.resolve('/example/nopick')
        self.assertEquals(example.show('request', 'nopick'), callback('request', *args, **kargs))
