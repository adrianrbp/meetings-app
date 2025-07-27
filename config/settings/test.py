"""
Testing settings.
"""

from .base import *
from .base import env

# I - Foundation
## 2. Security & App Identity
SECRET_KEY = env("DJANGO_SECRET_KEY", "django-insecure-3ad&4b*g9v#i0&@o!2xp!6258be+^2jmnb)s32q2zg_t-mau%9")
DEBUG = True
