from .main import *

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangogirls', #os.path.join(BASE_DIR, 'djangogirls')
        'USER': 'djangogirls',
        'PASSWORD': 'djangogirls',
        'HOST': '127.0.0.1',
        #'PORT': '5432'

    }
}
