"""
Base settings to build other settings files upon.
"""

import environ

env = environ.Env()

# I - Foundation
## 1. Project base directory: BASE_DIR / 'subdir'.
BASE_DIR = environ.Path(__file__) - 3
APPS_DIR = BASE_DIR.path('apps')

## 2. Dev Config
DEBUG = env.bool('DJANGO_DEBUG', False)

# II - Global
## 3. Internationalization (Time zone, language, etc.)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# III - Inner
## 4. Installed Apps (3rd party, Django core, and your own apps)
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = []

LOCAL_APPS = []

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# IV - Entry Point + Requests
## 5. WSGI Entry Point
WSGI_APPLICATION = 'config.wsgi.application'

## 6. URL Configuration
ROOT_URLCONF = 'config.urls'
ADMIN_URL = 'admin/'


## 7. Middleware Stack (Request/Response flow control)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# V - View + Files
## 8. Templates (Frontend HTML rendering system)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR.path('templates')),],
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
## 9. Static files (CSS, JS, Images)
STATIC_ROOT = str(BASE_DIR('staticfiles'))
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
]

MEDIA_ROOT = str(APPS_DIR('media'))
MEDIA_URL = '/media/'



# VI - Model
## 10. Database (define per environment)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

## 11. Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


## 12. Password validation
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
