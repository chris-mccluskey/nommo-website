import os
import dj_database_url
from .base import *


SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    'w(&_zuidtzbjcp+wvcyx!6+%j9-jdb48!z9kv8#r(9)k5h1&$y')
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = ['*']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
