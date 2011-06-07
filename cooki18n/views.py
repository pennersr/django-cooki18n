from django.conf import settings
from django import http
from django.utils.translation import check_for_language, activate, to_locale, get_language

def set_language(request):
    """
    Redirect to a given url while setting the chosen language in the
    session and cookie. The url and the language code need to be
    specified in the request parameters.
    The cookie will have a long expiration date (1 year) for future visits

    Since this view changes how the user will see the rest of the site, it must
    only be accessed as a POST request. If called as a GET request, it will
    redirect to the page in the request (the 'next' parameter) without changing
    any state.
    """
    next = request.REQUEST.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', None)
    if not next:
        next = '/'
    response = http.HttpResponseRedirect(next)
    if request.method == 'POST':
        lang_code = request.POST.get('language', None)
        if lang_code and check_for_language(lang_code):
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code, 365*24*60*60)
    return response
