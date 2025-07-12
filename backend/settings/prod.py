from . import *


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
