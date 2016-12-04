from django.conf import settings
from django.utils import translation
from django.utils.cache import patch_vary_headers
from django.utils.deprecation import MiddlewareMixin
from django.core.urlresolvers import get_resolver, LocaleRegexURLResolver

from . import utils


class LocaleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        check_path = self.is_language_prefix_patterns_used()
        language = utils.get_language_from_request(request, check_path=check_path)
        translation.activate(language)
        request.LANGUAGE_CODE = translation.get_language()

    def process_response(self, request, response):
        if settings.LANGUAGE_COOKIE_NAME not in response.cookies:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME,
                translation.get_language())
        patch_vary_headers(response, ('Accept-Language',))
        if 'Content-Language' not in response:
            response['Content-Language'] = translation.get_language()
        translation.deactivate()
        return response

    def is_language_prefix_patterns_used(self):
        """
        Returns `True` if the `LocaleRegexURLResolver` is used
        at root level of the urlpatterns, else it returns `False`.
        """
        for url_pattern in get_resolver(None).url_patterns:
            if isinstance(url_pattern, LocaleRegexURLResolver):
                return True
        return False
