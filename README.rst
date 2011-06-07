===============
django-cooki18n
===============

Django's builtin i18n support stores the selected language in the
session. This approach has the following problems:

- Sessions are created for anonymous users when they switch language
- It may lead to caching issues (the pages are set to "Vary-Cookie",
  but in fact the session cookie does not change when the language switches)

The above is captured in the following Django tickets.

- https://code.djangoproject.com/ticket/12794
- https://code.djangoproject.com/ticket/15902

This little project aims to be a drop in replacement for Django's i18n
so that you can have the language stored in a cookie, which is in line
with what ticket 12794 requests.

Installation
============

Simply follow the Django i18n instructions. However:

- Use ``cooki18n.middleware.LocaleMiddleware`` instead of ``django.middleware.locale.LocaleMiddleware``
- Use ``cooki18n.views.set_language`` instead of ``django.views.i18n.set_language``
- Use ``cooki18n.utils.get_language_from_request`` instead of ``django.utils.translation.get_language_from_request``
