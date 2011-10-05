from django.utils.cache import patch_vary_headers
from django.conf import settings
import re

class SubdomainMiddleware(object):
    def process_request(self, request):
        domain = settings.SITE_DOMAIN
        pattern = r'^(?:(?P<subdomain>.*?)\.)?%s(?::.*)?$' % re.escape(domain)
        matches = re.match(pattern, request.get_host())
        
        request.subdomain = None
        
        if matches:
            request.subdomain = matches.group('subdomain')
        return None

class SubdomainURLRoutingMiddleware(SubdomainMiddleware):
    def process_request(self, request):
        """
        Sets the current request's `urlconf` attribute to the URL conf 
        associated with the subdomain, if listed in `SUBDOMAIN_URLCONFS`.
        """
        super(SubdomainURLRoutingMiddleware, self).process_request(request)
        
        subdomain = getattr(request, 'subdomain', False)
        
        if subdomain is not False:
            try:
                request.urlconf = settings.SUBDOMAIN_URLCONFS[subdomain]
            except KeyError:
                # There was no match in the SUBDOMAIN_URLCONFS setting, so let the
                # ROOT_URLCONF handle the URL routing for this request.
                pass
        
        # Continue processing the request as normal.
        return None
    
    def process_response(self, request, response):
        """
        Forces the HTTP Vary header onto requests to avoid having responses
        cached from incorrect urlconfs.
        
        If you'd like to disable this for some reason, set `FORCE_VARY_ON_HOST`
        in your Django settings file to `False`.
        """
        if getattr(settings, 'FORCE_VARY_ON_HOST', True):
            patch_vary_headers(response, ('Host',))
        
        return response