import os


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1h@e+1z739!7!4x$1sftirie3m!es++i$2l84@5=d+gqlg*_ai'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django_editorjs',
    'django.contrib.sites',
    'corsheaders',
    'portfolio',
    'drf_yasg',
  'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
  "anymail",
 "whitenoise.runserver_nostatic",
  "django_tiptap",
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


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
##development
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
# DATABASES = {
#     'default': {
#      'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'Amezhiruth20!',
#         'PORT': '5432',
#         'HOST': 'db.jqlwshhbenltlnemngmn.supabase.co'

#     }
# }
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
# ##developments
STATIC_URL = '/static/'
STATICFILES_DIRS = [

    # os.path.join(BASE_DIR, 'static')

]
STATIC_ROOT = BASE_DIR/ 'assets'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/ 'media'

# STORAGES = {

#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }
# STATIC_HOST = "https://d4663kmspf1sqa.cloudfront.net"
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')





#production
# STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#   os.path.join(BASE_DIR, 'assets')
# ]

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')





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
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.zoho.com'
# EMAIL_HOST_USER = 'contact@ruthikegah.com'
# EMAIL_HOST_PASSWORD = 'Amezhiruth2'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
EMAIL_BACKEND = "anymail.backends.resend.EmailBackend"
ANYMAIL = {

    "RESEND_API_KEY": "re_3tMm8mUV_6L86ZQmmtLQxpyKfpUVaQ4LA",
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
DJANGO_TIPTAP_CONFIG = {
    "width": "500px",
    "height": "500px",
    "extensions": [
        # to see what each extension does, refer to [tiptap.dev](https://www.tiptap.dev/)
        "bold",
        "italic",
        "underline",
        "strikethrough",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "textAlign",
        "indent",
        "table",
        "bulletList",
        "orderedList",
        "typography",
        "clearFormat"
    ],
    "placeholderText": "Begin typing here...",  # set None to skip display
    "unsavedChangesWarningText": "You have unsaved changes",  # set None to skip display
    "lang": "EN",  # if you want to use default tooltips and translations, use this. Valid Options => EN/DE(for now)
    "tooltips": {
        # if you want to use your custom tooltips(maybe because you don't prefer default or the language you want isn't there)
        "bold": "Bold | (ctrl / ⌘) + B",
        "italic": "Italic | (ctrl / ⌘) + I",
        "underline": "Underline | (ctrl / ⌘) + U",
        "strike": "Strikethrough | (ctrl / ⌘) + shift + X",
        "h1": "Header 1 | (ctrl + alt) / (⌘ + ⌥) + 1",
        "h2": "Header 2 | (ctrl + alt) / (⌘ + ⌥) + 2",
        "h3": "Header 3 | (ctrl + alt) / (⌘ + ⌥) + 3",
        "h4": "Header 4 | (ctrl + alt) / (⌘ + ⌥) + 4",
        "h5": "Header 5 | (ctrl + alt) / (⌘ + ⌥) + 5",
        "h6": "Header 6 | (ctrl + alt) / (⌘ + ⌥) + 6",
        "alignLeft": "Align Left | (ctrl + shift ⇧) / (⌘ + shift ⇧) + L",
        "alignCenter": "Align Center | (ctrl + shift ⇧) / (⌘ + shift ⇧) + E",
        "alignRight": "Align Right | (ctrl + shift ⇧) / (⌘ + shift ⇧) + R",
        "alignJustify": "Justify | (ctrl + shift ⇧) / (⌘ + shift ⇧) + J",
        "indent": "Indent (Tab ↹)",
        "outdent": "Outdent (shift ⇧ + Tab ↹)",
        "bulletList": "Bullet List | (ctrl + shift ⇧) / (⌘ + shift ⇧) + 8",
        "orderedList": "Numbered List | (ctrl + shift ⇧) / (⌘ + shift ⇧) + 7",
        "addTable": "Add Table",
        "deleteTable": "Delete Table",
        "addColumnBefore": "Add Column Before",
        "addColumnAfter": "Add Column After",
        "deleteColumn": "Delete Column",
        "addRowBefore": "Add Row Before",
        "addRowAfter": "Add Row After",
        "deleteRow": "Delete Row",
        "mergeCells": "Merge Cells",
        "splitCell": "Split Cell",
        "toggleHeaderColumn": "Toggle Header Column",
        "toggleHeaderRow": "Toggle Header Row",
        "toggleHeaderCell": "Toggle Header Cell",
        "clearFormat": "Clear Format",
    },
    "translations": {
        # if the lang you defined exists in the default langs, then no need to define translations
        "row": "Row",
        "column": "Column",
        "add": "Add"
    },
    "custom_extensions": [],
    "tiptapOutputFormat": "html",  # options : "html", "json"

}
