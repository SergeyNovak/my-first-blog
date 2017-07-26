from .main import *

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'SergeyN$djangogirls',
        'USER': 'SergeyN',
        'PASSWORD': 'djangogirls',
        'HOST': 'SergeyN.mysql.pythonanywhere-services.com',

    }
}