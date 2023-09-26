from .base import *
import os

DEBUG = True

ADMINS = [
    ('Antonio M', 'email@mydomain.com'),
]

ALLOWED_HOSTS = ['tdnonline.com','www.tdnonline.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
