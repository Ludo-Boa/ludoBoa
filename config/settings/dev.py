from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')







CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"



# try:
#     from .local import *
# except ImportError:
#     pass
