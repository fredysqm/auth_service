"""
Django settings for otm project.
"""

from pathlib import Path
from .local import *

BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_URLCONF = 'main.urls'
WSGI_APPLICATION = 'main.wsgi.application'

STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  #3rd
  #'rest_framework',
  #me
  'accounts',
  'app',
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LANGUAGE_CODE = 'es-PE'
USE_I18N = True
USE_L10N = False
USE_TZ = True
TIME_ZONE = 'America/Lima'
DATETIME_FORMAT = 'd/m/Y H:i'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [Path.joinpath(BASE_DIR, 'templates'),],
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

STATICFILES_DIRS = (
  Path.joinpath(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp'

#Custom
if DEBUG:
  INTERNAL_IPS = ('127.0.0.1',)
  INSTALLED_APPS += ['debug_toolbar',]
  SLEEP_TIME = 1
  MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'app.middlewares.SleepMiddleware',
  ]
  DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
  ]
else: #PRODUCCION
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
  REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
      'rest_framework.renderers.JSONRenderer',
    ),
  }
  SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
  CACHES = {
    'default': {
      'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
      'LOCATION': 'localhost:11211',
    }
  }