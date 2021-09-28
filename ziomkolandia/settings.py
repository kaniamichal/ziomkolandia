"""
Django settings for ziomkolandia project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.conf.global_settings import STATIC_ROOT
from django.templatetags.static import static

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.ziomkolandia.pl', 'ziomkolandia.pl']
DEFAULT_CHARSET = 'utf-8'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'django.contrib.sites',
    'django.contrib.staticfiles',
    'django_extensions',
    'sorl.thumbnail',
    'tinymce',
    'website.apps.WebsiteConfig',
    'captcha',
    'newsletter',
    'blog',
    'cookielaw',
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

ROOT_URLCONF = 'ziomkolandia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'website/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'ziomkolandia.context_processors.blog_latest',
                'ziomkolandia.context_processors.blog_latest_pos4',
                'ziomkolandia.context_processors.blog_latest_pos3',
                'ziomkolandia.context_processors.blog_latest_pos2',
                'ziomkolandia.context_processors.blog_latest_pos1',
                'ziomkolandia.context_processors.blog_latest3',
                'ziomkolandia.context_processors.join_form',
                'cookielaw.context_processors.cookielaw',
            ],
        },
    },
]


WSGI_APPLICATION = 'ziomkolandia.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'm1470_ziomk',
        'USER': 'm1470_ziomek',
        'PASSWORD': 'Kemoiz12La3',
        'HOST': 'mysql54.mydevil.net',
        'PORT': 3306,
    }
}


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


# newsletter
NEWSLETTER_THUMBNAIL = 'sorl-thumbnail'
NEWSLETTER_CONFIRM_EMAIL = True
NEWSLETTER_CONFIRM_EMAIL_SUBSCRIBE = True
NEWSLETTER_CONFIRM_EMAIL_UNSUBSCRIBE = True
NEWSLETTER_CONFIRM_EMAIL_UPDATE = True
NEWSLETTER_RICHTEXT_WIDGET = "tinymce.widgets.TinyMCE"

LANGUAGE_CODE = 'pl-pl'

TIME_ZONE = 'Europe/Warsaw'
USE_TZ = False

USE_I18N = True

USE_L10N = True

CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_MATH_CHALLENGE_OPERATOR = '+'
CAPTCHA_TIMEOUT = '15'
CAPTCHA_BACKGROUND_COLOR = 'white'
CAPTCHA_FOREGROUND_COLOR = 'black'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'info@ziomkolandia.pl'
EMAIL_HOST = 'az0024.srv.az.pl'
EMAIL_HOST_USER = 'noreply@ziomkolandia.pl'
EMAIL_HOST_PASSWORD = 'Zima2021!@#'
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_SUBJECT_PREFIX = 'ZIOMKOLANDIA.PL :'
EMAIL_USE_LOCALTIME = True

DATETIME_FORMAT = 'E d, Y, H'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "website/templates/static"]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS settings
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True



# STATIC_ROOT = [BASE_DIR, 'public', 'static', 'staticfiles']

# anothe settings for newsletter
TINYMCE_JS_URL = os.path.join(STATIC_URL, "path/to/tiny_mce/tiny_mce.js")
# TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "path/to/tiny_mce")
TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "width": "960px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
               "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
               "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
               "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
               "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
               "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
    "language": "pl-pl",  # To force a specific language instead of the Django current language.
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True
