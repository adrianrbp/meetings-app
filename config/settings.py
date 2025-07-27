import os
from pathlib import Path

# 1. Project base directory: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# 2. Security & App Identity
# Use environment variables for production
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "django-insecure-3ad&4b*g9v#i0&@o!2xp!6258be+^2jmnb)s32q2zg_t-mau%9")
DEBUG = True
ALLOWED_HOSTS = []


# 3. Installed Apps (3rd party, Django core, and your own apps)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# 4. Middleware Stack (Request/Response flow control)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 5. URL Configuration
ROOT_URLCONF = 'config.urls'

# 6. Templates (Frontend HTML rendering system)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# 7. WSGI Entry Point
WSGI_APPLICATION = 'config.wsgi.application'

# 8. Database (define per environment)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# 9. Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# 10. Internationalization (Time zone, language, etc.)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# 11. Static files (CSS, JS, Images)
STATIC_URL = 'static/'

# 12. Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
