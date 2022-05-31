<<<<<<< HEAD:ouest/settings/settings.py
from pathlib import Path
import environ
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
environ.Env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
=======

import os
import environ
env = environ.Env()
environ.Env.read_env()

from pathlib import Path
>>>>>>> 9fbfc94279852f12c84bcda9c34a8e57e8403a68:ouest/settings.py

SECRET_KEY = env('SECRET_KEY')



DEBUG = env('DEBUG')
# Allowed host for production
ALLOWED_HOSTS= ['ouestsenegal.herokuapp.com', '127.0.0.1']
# Allowed host for developement

# ALLOWED_HOSTS = ['.ouestsenegal.herokuapp.com']
# if not DEBUG:
#     ALLOWED_HOSTS += env('ALLOWED_HOSTS')

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'ckeditor',
    'ckeditor_uploader',
    'storages',
<<<<<<< HEAD:ouest/settings/settings.py
    # 'taggit',
=======
>>>>>>> 9fbfc94279852f12c84bcda9c34a8e57e8403a68:ouest/settings.py

    'blog',
    'core',
    'content',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ouest.urls'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_EMAIL_VERIFICATION = "none"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.views.categories',
            ],
        },
    },
]
WSGI_APPLICATION = 'ouest.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env('POSTGRES_NAME'),
            'USER': env('POSTGRES_USER'),
            'PASSWORD': env('POSTGRES_PASSWORD'),
            'HOST': env('POSTGRES_HOST'),
            'PORT': env('POSTGRES_PORT'),
            'keepalives':1,
            'keepalives_idle':130,
            'keepalives_interval':10,
            'keepalives_count':15
    }
}


import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default'].update(db_from_env)


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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

<<<<<<< HEAD:ouest/settings/settings.py
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

=======
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL='/static/'
MEDIA_URL = '/media/'
>>>>>>> 9fbfc94279852f12c84bcda9c34a8e57e8403a68:ouest/settings.py
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
<<<<<<< HEAD:ouest/settings/settings.py
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_root/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
=======
>>>>>>> 9fbfc94279852f12c84bcda9c34a8e57e8403a68:ouest/settings.py

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DJANGO_WYSIWYG_FLAVOR = "ckeditor"
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_BROWSE_SHOW_DIRS = True 
CKEDITOR_RESTRICT_BY_DATE = True
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}

SITE_ID=1


AWS_S3_ACCESS_KEY_ID=env('AWS_S3_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY=env('AWS_S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME=env('AWS_STORAGE_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE=False
AWS_DEFAULT_ACL=None

DEFAULT_FILE_STORAGE='storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'





<<<<<<< HEAD:ouest/settings/settings.py
SITE_ID = 1

#S3 BUCKETS CONFIG

# AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID'),
# AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY'),
# AWS_S3_BUCKET_NAME_STATIC  = env('AWS_STORAGE_BUCKET_NAME'),

# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# AWS
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'ouestsenegal'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
=======
>>>>>>> 9fbfc94279852f12c84bcda9c34a8e57e8403a68:ouest/settings.py
