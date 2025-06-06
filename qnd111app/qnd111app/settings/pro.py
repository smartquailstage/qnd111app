from .base_prod import *

import os  # Asegúrate de importar os si no está importado

DEBUG = True

ALLOWED_HOSTS = ['*']

# -------------------------------------------
# Wagtail AI (comentado por ahora)
# -------------------------------------------
# import wagtail_ai
# WAGTAIL_AI_PROMPTS = wagtail_ai.DEFAULT_PROMPTS + [
#     {
#         "label": "Simplify",
#         "description": "Rewrite your text in a simpler form",
#         "prompt": "Rewrite the following text to make it simpler and more succinct",
#         "method": "replace",
#     }
# ]

# -------------------------------------------
# Seguridad (comentados, pero bien)
# -------------------------------------------
# CSRF_COOKIE_DOMAIN = ".www.smartquail.io"
# CSRF_COOKIE_SECURE = True
# CSRF_TRUSTED_ORIGINS = ['https://www.smartquail.io', 'https://146.190.164.22']
# CORS_ALLOWED_ORIGINS = [
#     'https://www.smartquail.io', 'https://146.190.164.22'
# ]

# -------------------------------------------
# Wagtail embeds
# -------------------------------------------
WAGTAILEMBEDS_RESPONSIVE_HTML = True

# -------------------------------------------
# Base de datos (SQLite por defecto)
# -------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# -------------------------------------------
# Configuración PostgreSQL a partir de variables de entorno
# -------------------------------------------
DB_USERNAME = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_DATABASE = os.environ.get("POSTGRES_DB")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_ENGINE = os.environ.get("POSTGRES_ENGINE")

DB_IS_AVAILABLE = all([DB_USERNAME, DB_PASSWORD, DB_DATABASE, DB_HOST, DB_PORT])

if DB_IS_AVAILABLE:
    DATABASES = {
        'default': {
            'ENGINE': DB_ENGINE,
            'NAME': DB_DATABASE,
            'USER': DB_USERNAME,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
        }
    }

# -------------------------------------------
# Django default primary key field type
# -------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------------------------
# Email setup
# -------------------------------------------
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT') or 25)  # Cast a int y default 25
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')  # Quité espacio extra
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = False

# -------------------------------------------
# Redis & Celery setup
# -------------------------------------------
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
REDIS_DB = os.environ.get('REDIS_DB', '0')

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

# -------------------------------------------
# Cache (Redis)
# -------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f"redis://{REDIS_HOST}:{REDIS_PORT}/1",
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# -------------------------------------------
# Social Auth
# -------------------------------------------
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = os.environ.get('SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET = os.environ.get('SOCIAL_AUTH_TWITTER_SECRET')

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

# -------------------------------------------
# Twilio
# -------------------------------------------
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_FROM = os.environ.get("TWILIO_WHATSAPP_FROM")

# -------------------------------------------
# Configuración AWS / DigitalOcean Spaces
# -------------------------------------------
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = os.environ.get("AWS_S3_ENDPOINT_URL", "").rstrip('/')  # Remueve slash al final si existe

AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
    "ACL": "public-read",  # Cambiar a 'private' si quieres privacidad
}

AWS_LOCATION = os.environ.get("AWS_LOCATION", "static")  # valor por defecto 'static'

# -------------------------------------------
# Almacenamiento de archivos estáticos y media
# -------------------------------------------
STATICFILES_STORAGE = os.environ.get("STATICFILES_STORAGE")
DEFAULT_FILE_STORAGE = os.environ.get("MEDIA_STORAGE")

STATIC_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/"
MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/media/"

# -------------------------------------------
# Si necesitas STATIC_ROOT (para collectstatic local)
# -------------------------------------------
# STATIC_ROOT = os.path.join(BASE_DIR, "static_collected")  # descomenta si usas localmente

