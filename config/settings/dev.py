from .base import *


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
