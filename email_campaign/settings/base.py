import os
from datetime import timedelta
from pathlib import Path

from decouple import config
from django.utils.translation import gettext_lazy as _


PRODUCTION = config("PRODUCTION", default=False, cast=bool)
DEBUG = config("DEBUG", default=False, cast=bool)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DJANGO_SETTINGS_MODULE = 'email_campaign.settings.base'

DOCS_URL = config("DOCS_URL")
ADMIN_URL = config("ADMIN_URL")

LOCAL_APPS = [
    "src.common.apps.CommonConfig",
    "src.campaigns.apps.CampaignsConfig",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
    "debug_toolbar",
    "simple_history",
    "drf_spectacular",
    "drf_spectacular_sidecar",
]

THEME_APPS = [
    "jazzmin",
]


INSTALLED_APPS = [
    *THEME_APPS,
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

ROOT_URLCONF = "email_campaign.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "email_campaign.wsgi.application"

TIME_ZONE = "UTC"
DATE_FORMAT = "%Y-%m-%d"
USE_TZ = True

LANGUAGE_CODE = "ru"
USE_I18N = True
USE_L10N = True
LANGUAGES = (
    ("ru", _("Russian")),
    ("en", _("English")),
    ("ky", _("Kyrgyz")),
)
LANGUAGE_COOKIE_NAME = "lang"

LOCALE_PATHS = [f"{BASE_DIR}/common/locale"]

DATA_UPLOAD_MAX_MEMORY_SIZE = None

# Static files
STATIC_URL = "/back_static/"
STATIC_ROOT = os.path.join(BASE_DIR, "back_static")

# Media files
MEDIA_URL = "/back_media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "back_media")

X_FRAME_OPTIONS = "SAMEORIGIN"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 15,
    "DATE_FORMAT": "%d.%m.%Y",
    "TIME_FORMAT": "%H:%M",
    "DATE_INPUT_FORMATS": ["%d.%m.%Y", "%d-%m-%Y", "%Y-%m-%d", "%Y.%m.%d"],
    "DEFAULT_RENDERER_CLASSES": (
        ["rest_framework.renderers.JSONRenderer"]
        if PRODUCTION and not DEBUG
        else [
            "rest_framework.renderers.JSONRenderer",
            "rest_framework.renderers.BrowsableAPIRenderer",
        ]
    ),
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Email Campaign API",
    "DESCRIPTION": "Swagger OpenAPI Scheme for Email Campaign's api endpoint",
    "VERSION": "1.0.0",
    "OAS_VERSION": "3.0.3",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
    },
    "REDOC_UI_SETTINGS": {
        "deepLinking": True,
    },
    "SWAGGER_UI_DIST": "SIDECAR",  # shorthand to use the sidecar instead
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
}

AUTH_USER_MODEL = "auth.User"

EMAIL_BACKEND = config("EMAIL_BACKEND")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool)

REDIS_HOST = config("REDIS_HOST")
REDIS_PORT = config("REDIS_PORT")
REDIS_DB = config("REDIS_DB")

CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"
CELERY_BROKER_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}"
CELERY_BROKER_CONNECTION_RETRY = True
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

from .cors import *
from .themes import *

if not PRODUCTION:
    from .dev import *
else:
    from .prod import *

if DEBUG:
    INTERNAL_IPS = ["127.0.0.1"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
