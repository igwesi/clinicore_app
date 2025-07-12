import os
import environ
from pathlib import Path


env = environ.Env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.'+env('DJANGO_ENV'))

application = get_wsgi_application()
