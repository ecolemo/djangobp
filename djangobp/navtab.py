class ActiveTabMiddleware(object):
    def process_request(self, request):
        if 'active_tab' in request.COOKIES:
            request.active_tab = request.COOKIES['active_tab']

    def process_response(self, request, response):
        if hasattr(request, 'active_tab'):
            response.set_cookie('active_tab', request.active_tab)
        return response