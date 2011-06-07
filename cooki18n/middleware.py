from django.conf import settings
from django.utils import translation
from django.utils.cache import patch_vary_headers

from utils import get_language_from_request

class LocaleMiddleware(object):
    def process_request(self, request):
        language = get_language_from_request(request)
        translation.activate(language)
        request.LANGUAGE_CODE = translation.get_language()

    def process_response(self, request, response):
        if not response.cookies.has_key(settings.LANGUAGE_COOKIE_NAME): 
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, translation.get_language()) 
        patch_vary_headers(response, ('Accept-Language',))
        if 'Content-Language' not in response:
            response['Content-Language'] = translation.get_language()
        translation.deactivate()
        return response
