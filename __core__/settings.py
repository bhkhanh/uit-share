"""
For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from decouple import config, Csv
import dj_database_url

# ============================================================
# CORE Settings
# ============================================================

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

ROOT_URLCONF = '__core__.urls'

WSGI_APPLICATION = '__core__.wsgi.application'

# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "uitshare_user.User"

LOGIN_REDIRECT_URL = "home-page"

# ============================================================
# Application definition
# ============================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.postgres",
    "widget_tweaks",
    "uitshare_main",
    "uitshare_user",
    "uitshare_search",
    "storages",
    "uitshare_search.templatetags",
]

# ============================================================
# MIDDLEWARE Settings
# ============================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",   # WhiteNoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ============================================================
# TEMPLATES Settings
# ============================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",
        ],
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

# ============================================================
# DATABASES Settings
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# ============================================================

DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL"),
        conn_max_age=0,
    ),
}

# ============================================================
# AUTHENTICATION & AUTHORIZATION Settings
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
# ============================================================

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

# ============================================================
# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
# ============================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = config("TIME_ZONE")

USE_I18N = True

USE_TZ = True

# ============================================================
# STATIC FILES Settings (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# ============================================================

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "static_files"

# Using WhiteNoise for Static files Storage
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ============================================================
# MEDIA FILES Settings (using AWS S3 Settings in this project)
# ============================================================

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_S3_FILE_OVERWRITE = config("AWS_S3_FILE_OVERWRITE", cast=bool)
AWS_QUERYSTRING_AUTH = config("AWS_QUERYSTRING_AUTH", cast=bool)
AWS_DEFAULT_ACL = config("AWS_DEFAULT_ACL")
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME")
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"

MEDIA_ROOT = f"https://{AWS_S3_CUSTOM_DOMAIN}/"


# ============================================================
# SECURE Settings
# https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
# ============================================================

SECURE_HSTS_SECONDS = config("SECURE_HSTS_SECONDS", cast=int)
SECURE_HSTS_PRELOAD = config("SECURE_HSTS_PRELOAD", cast=bool)
SECURE_HSTS_INCLUDE_SUBDOMAINS = config("SECURE_HSTS_INCLUDE_SUBDOMAINS", cast=bool)
SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", cast=bool)
SESSION_COOKIE_SECURE = config("SESSION_COOKIE_SECURE", cast=bool)
SECURE_BROWSER_XSS_FILTER = config("SECURE_BROWSER_XSS_FILTER", cast=bool)
CSRF_COOKIE_SECURE = config("CSRF_COOKIE_SECURE", cast=bool)

# Set session timeout in 120 minutes (2 hours)
SESSION_COOKIE_AGE = config("SESSION_COOKIE_AGE", cast=int)


# ============================================================
# EMAIL Settings
# ============================================================

# for development
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# for production
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = config("EMAIL_PORT", cast=int)
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool)
EMAIL_USE_LOCALTIME = config("EMAIL_USE_LOCALTIME", cast=bool)
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")

# The number of seconds a password reset link is valid for.
PASSWORD_RESET_TIMEOUT = config("PASSWORD_RESET_TIMEOUT", cast=int)