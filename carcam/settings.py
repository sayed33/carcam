from pathlib import Path
import os
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

BASE_DIR = Path(__file__).resolve().parent.parent

# الأمن وبيئة التشغيل
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-...')
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 'yes')
ALLOWED_HOSTS = os.getenv(
    'ALLOWED_HOSTS',
    'hamdicrypto.pythonanywhere.com,carcam-s9l5.onrender.com,localhost,127.0.0.1'
).split(',')


# التطبيقات
INSTALLED_APPS = [
    'cloudinary',
    'cloudinary_storage',
    'camera',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# ملفات الميديا (صور Cloudinary)
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME', 'dzn2vthfn'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY', '876612625865211'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET', '-s520ao3ATq6zECp-T59Ts2zH-c'),
}

# ملفات static
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'camera' / 'static']
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# لتأكد من العثور على ملفات static
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# الميدل وير
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # مهم جدًا لـ Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'carcam.urls'

# القوالب
TEMPLATES = [{
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
}]

WSGI_APPLICATION = 'carcam.wsgi.application'

# قاعدة البيانات (PostgreSQL أو SQLite)
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600,
        ssl_require=False
    )
}

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# الإعدادات العالمية
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# الإعداد الافتراضي لمفتاح الـ PK
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
