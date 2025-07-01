from pathlib import Path
import os
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# سر المشروع
SECRET_KEY = 'django-insecure-ynat))ntgvxj7rkmf7g5fz7nm-cooh_h$a^4lun=ufc5r1c*r9'

# لا تفعّل DEBUG في الإنتاج
DEBUG = False

# الهوستات المسموح بها
ALLOWED_HOSTS = ['carcam-s9l5.onrender.com', 'localhost', '127.0.0.1']

# التطبيقات المثبتة
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

# إعدادات Cloudinary للصور/الملفات
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dzn2vthfn',
    'API_KEY': '876612625865211',
    'API_SECRET': '-s520ao3ATq6zECp-T59Ts2zH-c',
}

# إعدادات ملفات static
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # سيجمع الملفات هنا عند collectstatic
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# لو عندك ملفات static مخصصة في مجلد معين، فعل السطر ده:
# STATICFILES_DIRS = [BASE_DIR / 'camera' / 'static']

# إعدادات Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # لخدمة static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# إعدادات URLs
ROOT_URLCONF = 'carcam.urls'

# إعدادات القوالب
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

# WSGI
WSGI_APPLICATION = 'carcam.wsgi.application'

# إعدادات قاعدة البيانات
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3'),
        conn_max_age=600,
    )
}

# تحقق كلمات المرور
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

# إعدادات اللغة والوقت
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# نوع الـ primary key الافتراضي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
