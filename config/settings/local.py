"""
Development settings.
"""

from .base import *
from .base import env

# I - Foundation
## 2. Security & App Identity
SECRET_KEY = env("DJANGO_SECRET_KEY", default="django-insecure-3ad&4b*g9v#i0&@o!2xp!6258be+^2jmnb)s32q2zg_t-mau%9")
DEBUG = True
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]
# III - Inner
## 4. Dev-only apps (e.g., debug toolbar)
# INSTALLED_APPS += [
#     "debug_toolbar",
# ]


# IV - Entry Point + Requests
## 7. Dev-only middleware
# MIDDLEWARE += [
#     "debug_toolbar.middleware.DebugToolbarMiddleware",
# ]

# 7.1. Reload Debug Toolbar
# INTERNAL_IPS = [
#     "127.0.0.1",
# ]

# V - View + Files
# 9. Static & Media files
# STATICFILES_DIRS += [BASE_DIR / "dev_static"]
MEDIA_ROOT = str(APPS_DIR('media'))
MEDIA_URL = '/media/'
# 13. Local email backend (prints to console)
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
