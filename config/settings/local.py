from .base import *

# 2. Local Dev Settings
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# 3. Dev-only apps (e.g., debug toolbar)
# INSTALLED_APPS += [
#     "debug_toolbar",
# ]

# 4. Dev-only middleware
# MIDDLEWARE += [
#     "debug_toolbar.middleware.DebugToolbarMiddleware",
# ]

# 14. Reload Debug Toolbar
# INTERNAL_IPS = [
#     "127.0.0.1",
# ]


# 11. Static & Media files
# STATICFILES_DIRS += [BASE_DIR / "dev_static"]
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# 13. Local email backend (prints to console)
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
