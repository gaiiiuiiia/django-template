from ._base import *

DEBUG = True
ALLOWED_HOSTS = [
    '127.0.0.1',
    '0.0.0.0',
]

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG,
}
