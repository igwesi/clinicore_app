from . import *

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',   
        'HOST': env("DB_HOST"),
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PORT': env("DB_PORT"),
        'PASSWORD': env("DB_PASSWORD"),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
