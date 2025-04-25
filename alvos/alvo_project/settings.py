import environ
import os

env = environ.Env()

#arquivo .env
environ.Env.read_env('C:/Users/vhenr/OneDrive/Área de Trabalho/alvo_projects/.env')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'alvos', 
]

# Configuração do banco de dados usando variáveis do .env
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),  # Nome do banco de dados
        'USER': env('DB_USER'),  # Usuário do banco de dados
        'PASSWORD': env('DB_PASSWORD'),  # Senha do banco de dados
        'HOST': env('DB_HOST', default='localhost'),  # Host do banco de dados (padrão: localhost)
        'PORT': env('DB_PORT', default='5432'),  # Porta do banco de dados (padrão: 5432)
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  
    'django.contrib.messages.middleware.MessageMiddleware', 
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# Configuração de ALLOWED_HOSTS
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', 'localhost:8000']

# Configuração de ROOT_URLCONF
ROOT_URLCONF = 'alvos.urls'

SECRET_KEY = env('SECRET_KEY', default='admin') 

DEBUG = env.bool('DEBUG', default=False)  # carrega o modo de depuração do .env

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = 'static/' 
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 