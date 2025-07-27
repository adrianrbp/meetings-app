from .base import *
from .base import env

# I - Foundation
## 2. Security & App Identity
SECRET_KEY = env('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['sample.io'])

# III - Inner
## 4. Gunicorn
INSTALLED_APPS += ['gunicorn']


# IV - Entry Point + Requests
## 6. URL Configuration
ADMIN_URL = env('DJANGO_ADMIN_URL')


# VII - Extras
# LOGGING = {}