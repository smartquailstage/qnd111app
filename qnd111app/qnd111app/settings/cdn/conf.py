import os

# Configuración de AWS y DigitalOcean Spaces
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

# Asegúrate de que AWS_S3_ENDPOINT_URL no sea None antes de llamar a rstrip
endpoint_url = os.environ.get("AWS_S3_ENDPOINT_URL", "")
AWS_S3_ENDPOINT_URL = endpoint_url.rstrip('/') if endpoint_url else ""

AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
    "ACL": "public-read"  # Cambia a 'private' si quieres archivos privados
}

# Ubicación dentro del bucket ('static' o 'media'), con valor por defecto
AWS_LOCATION = os.environ.get("AWS_LOCATION", "static")

# URLs públicas para los archivos estáticos y media
STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/' if AWS_S3_ENDPOINT_URL else "/static/"
MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/media/' if AWS_S3_ENDPOINT_URL else "/media/"

# Backends de almacenamiento para archivos estáticos y media
STATICFILES_STORAGE = os.environ.get("STATICFILES_STORAGE")
DEFAULT_FILE_STORAGE = os.environ.get("MEDIA_STORAGE")

# Configuración específica para DigitalOcean Spaces con firma v4
AWS_S3_SIGNATURE_VERSION = 's3v4'