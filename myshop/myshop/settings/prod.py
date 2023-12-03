from .base import *
import os

DEBUG = False

ADMINS = [
    ('Alejandro R', 'alememe45@gmail.com'),
]

ALLOWED_HOSTS = ['www.compufacil.store','compufacil.store','128.199.6.12']

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
