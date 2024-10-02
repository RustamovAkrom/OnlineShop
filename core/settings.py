from django.utils.translation import gettext_lazy

from dotenv import load_dotenv
import os

load_dotenv()

from core.config import *
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1', 
    'localhost',
    'onlineshop-d42t.onrender.com',
]

INSTALLED_APPS = DEFAULT_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
INTERNAL_IPS = [
    "127.0.0.1",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.cart.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_L10N = True

USE_TZ = True


def gettext(s):
    return gettext_lazy(s)


LANGUAGES = [
    ("en", gettext("English")),
    ("ru", gettext("Русский")),
    ("uz", gettext("O`zbekcha")),
]

LOCALE_PATHS = [
    BASE_DIR.joinpath("locale"),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = "en"
MODELTRANSLATION_LANGUAGES = ("en", "uz", "ru")
MODELTRANSLATION_FALLBACK_LANGUAGES = ("en", "uz", "ru")


STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR.joinpath("static")]
STATIC_ROOT = BASE_DIR.joinpath("staticfiles")

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR.joinpath("media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CART_SESSION_ID = "cart"
