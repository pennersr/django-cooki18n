from django.utils.translation import get_language_from_request as _get_language_from_request


class RequestWithoutSession(object):
    def __init__(self, wrapped):
        object.__setattr__(self, 'inner', wrapped)

    def __getattr__(self, attr):
        if attr == 'session':
            raise AttributeError
        return getattr(self.inner, attr)

    def __setattr__(self, attr, value):
        return setattr(self.inner, attr, value)


def get_language_from_request(request, **kwargs):
    return _get_language_from_request(RequestWithoutSession(request), **kwargs)
