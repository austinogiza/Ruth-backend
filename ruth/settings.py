import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!


## development
ALLOWED_HOSTS = []
DEBUG = True
## production
# DEBUG = False ## production
# ALLOWED_HOSTS = ["www.api.ruthikegah.com", "api.ruthikegah.com"]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.sites',
    'corsheaders',
    'portfolio',
    'drf_yasg',
    'rest_framework',
    "anymail",
    "whitenoise.runserver_nostatic",
    "django_tiptap",
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
      "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
ROOT_URLCONF = 'ruth.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
      'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'ruth.wsgi.application'


##development
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'ruth',
#         'USER': 'postgres',
#         'PASSWORD': 'austinforreal',
#         'PORT': '5433',
#         'HOST': 'localhost'

#     }
# }

## production
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'ruth',
#         'USER': 'ruth',
#         'PASSWORD': 'ruth',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# DATABASES = {
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ruth',
        'USER': 'postgres',
        'PASSWORD': 'austinforreal',
        'PORT': '5433',
        'HOST': 'localhost'

    }
}
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',

    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
##developments
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [

#     # os.path.join(BASE_DIR, 'static')

# ]
# STATIC_ROOT = BASE_DIR / "staticfiles"
# STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# CKEDITOR_UPLOAD_PATH = "uploads/"



#production
# STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#   os.path.join(BASE_DIR, 'assets')
# ]

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')






#production
STATIC_URL = '/static/'

STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'assets')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')





DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
     "http://localhost:3001",
     "https://www.ruthikegah.com",
     "https://ruthikegah.com"


]
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_UNIQUE_EMAIL = True

EMAIL_BACKEND = "anymail.backends.resend.EmailBackend"
ANYMAIL = {

    "RESEND_API_KEY": os.environ.get('RESEND_API_KEY'),
}
# EMAIL_USE_SSL = False
#
DEFAULT_FROM_EMAIL = 'contact@ruthikegah.com'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'user.serializers.CustomRegisterSerializer',
    "PASSWORD_RESET_SERIALIZER": "dj_rest_auth.serializers.PasswordResetSerializer",
    "PASSWORD_RESET_CONFIRM_SERIALIZER": "dj_rest_auth.serializers.PasswordResetConfirmSerializer",
}
SITE_ID = 1
