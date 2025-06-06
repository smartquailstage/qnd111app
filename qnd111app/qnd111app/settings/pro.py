from .base_prod import *



DEBUG=True

# Obtener las variables de entorno desde Kubernetes
IP = os.environ.get("IP")
DOMAIN = os.environ.get("DOMAIN")
HOST = os.environ.get("HOST")

ALLOWED_HOSTS='127.0.0.1',"localhost","https://qnd111.smartquail.io","qnd111.smartquail.io","64.23.178.103"

#import wagtail_ai

#WAGTAIL_AI_PROMPTS = wagtail_ai.DEFAULT_PROMPTS + [
#    {
#        "label": "Simplify",
#        "description": "Rewrite your text in a simpler form",
#        "prompt": "Rewrite the following text to make it simper and more succinct",
#        "method": "replace",
#    }
#]


#CSRF_COOKIE_DOMAIN="http://qnd03101.smartquail.io"
#CSRF_COOKIE_SECURE = True
#CSRF_TRUSTED_ORIGINS = ['https://qnd03101.smartquail.io','https://meddes.smartquail.io/','https://146.190.164.22']
CORS_ALLOWED_ORIGINS = [
    'https://qnd111.smartquail.io','https://qnd111.smartquail.io/ingresar'
    # Otros orígenes permitidos si los hay
]





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Obtención de variables de entorno para la configuración de PostgreSQL
DB_USERNAME = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_DATABASE = os.environ.get("POSTGRES_DB")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_ENGINE = os.environ.get("POSTGRES_ENGINE")

# Verificación de disponibilidad de las variables necesarias para PostgreSQL
DB_IS_AVAILABLE = all([
    DB_USERNAME,
    DB_PASSWORD,
    DB_DATABASE,
    DB_HOST,
    DB_PORT
])

# Configuración condicional para PostgreSQL
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

#Static files DevMod





from .cdn.conf import * #noqa




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# celery setup



#Email setups
EMAIL_HOST          = os.environ.get('EMAIL_HOST')
EMAIL_PORT          =  os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER     = os.environ.get('EMAIL_HOST_USER ')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL  = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS       = False
#EMAIL_USE_SSL       = False


REDIS_HOST=os.environ.get('REDIS_HOST')
REDIS_PORT=os.environ.get('REDIS_PORT')
REDIS_DB =os.environ.get('REDIS_DB')  

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60 


# social auth settings
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = os.environ.get('SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET =  os.environ.get('SOCIAL_AUTH_TWITTER_SECRET')

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET ')




CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}

# settings.py

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# celery setup

# celery setup





CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}





# Configuración de serialización actualizada (según las advertencias)
accept_content = ['json']  # Esto reemplaza 'CELERY_ACCEPT_CONTENT'
task_serializer = 'json'   # Esto reemplaza 'CELERY_TASK_SERIALIZER'
result_serializer = 'json'  # Esto reemplaza 'CELERY_RESULT_SERIALIZER'

# Si deseas mantener el comportamiento de reconexión automática en el inicio del broker, usa:
#broker_connection_retry_on_startup = True


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'  # Para Gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'phys.mauricio.silva@gmail.com'  # Tu correo de Gmail
EMAIL_HOST_PASSWORD = '1719183830'  # La contraseña de tu cuenta de Gmail
DEFAULT_FROM_EMAIL = 'phys.mauricio.silva@gmail.com'




TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")



# Configuración de AWS
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = os.environ.get("AWS_S3_ENDPOINT_URL")  # Cambia si usas otro endpoint
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400", 
    "ACL": "public-read"  # Cambia a 'private' si los archivos deben ser privados
}

# Configuración de almacenamiento
AWS_LOCATION = os.environ.get("AWS_LOCATION")  # 'static' o 'media'

# Asegúrate de que la URL de los archivos estáticos esté correcta
STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/'