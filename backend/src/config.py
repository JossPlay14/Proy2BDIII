import os
from datetime import timedelta
from dotenv import load_dotenv
from .utils.utils import str_to_bool

# Carga .env.production en producción, .env en desarrollo
load_dotenv('.env.production' if os.getenv('FLASK_ENV') == 'production' else '.env')

class Config:
    # Configuración de la API
    API_TITLE = os.getenv("API_TITLE", "Streaming API")  # Valor por defecto
    API_DESCRIPTION = os.getenv("API_DESCRIPTION", "API para plataforma de streaming")
    API_VERSION = os.getenv("API_VERSION", "1.0")
    API_PREFIX = os.getenv("API_PREFIX", "api")

    # Configuración del servidor
    PORT = int(os.getenv("PORT", "10000"))  # Render usa puerto 10000 por defecto
    DEBUG = str_to_bool(os.getenv("DEBUG", "False"))  # False en producción

    # Configuración CORS
    DEFAULT_ORIGINS = "http://localhost:3000,http://localhost:5000"
    ORIGINS = os.getenv("ORIGINS", DEFAULT_ORIGINS).split(",")

    # Configuración JWT
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    if not JWT_SECRET_KEY:
        raise ValueError("JWT_SECRET_KEY no está configurada")

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        minutes=float(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", "60"))  # 60 minutos por defecto
    )
    JWT_COOKIE_SECURE = str_to_bool(os.getenv("JWT_COOKIE_SECURE", "True"))  # True en producción
    JWT_TOKEN_LOCATION = os.getenv("JWT_TOKEN_LOCATION", "cookies").split(",")
    JWT_COOKIE_CSRF_PROTECT = str_to_bool(os.getenv("JWT_COOKIE_CSRF_PROTECT", "True"))  # True en producción
    JWT_ACCESS_COOKIE_NAME = os.getenv("JWT_ACCESS_COOKIE_NAME", "access_token")

    # Configuración MongoDB
    MONGO_URI = os.getenv("MONGO_URI")
    if not MONGO_URI:
        raise ValueError("MONGO_URI no está configurada")

    # Configuración Redis
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

    # Configuración de usuarios
    USERS_PASSWORD = os.getenv("USERS_PASSWORD", "defaultSecurePassword123!")  # Cambiar en producción
