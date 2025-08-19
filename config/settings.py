from pathlib import Path
import os
import environ

# 環境変数の読み込み
env = environ.Env()
environ.Env.read_env()

# BASE_DIR の定義
BASE_DIR = Path(__file__).resolve().parent.parent

# セキュリティ
SECRET_KEY = env("SECRET_KEY")
DEBUG = True  # 本番では False にする
ALLOWED_HOSTS = []

# アプリケーション定義
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'diary',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'private_diary' / 'templates'],  # ←共通テンプレートを明示
        'APP_DIRS': True,  # ←各アプリの templates/ も自動で探索
        'OPTIONS': {'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ]},
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# データベース設定（PostgreSQL）
# どちらかを使えるように：DATABASE_URL があればそれを優先
# 例: .env に DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
if env('DATABASE_URL', default=None):
    DATABASES = {'default': env.db('DATABASE_URL')}
else:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT', default='5432'),
    }
}

# パスワードバリデーション
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 認証後のリダイレクト
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'diary:diary_list'
LOGOUT_REDIRECT_URL = 'diary:login'  # ← 必要に応じて使用

# タイムゾーンと言語
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True

# 静的ファイル
STATIC_URL = '/static/'

# デフォルトの主キーの型
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 開発用メールバックエンド：送信せずコンソールに出力
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# サイトのドメイン/プロトコル（リセットURL組み立て用）
DEFAULT_FROM_EMAIL = "no-reply@example.com"

DEBUG = env.bool('DEBUG', default=True)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])  # 例: ['your-domain.com', 'localhost']

# 例： https を使う本番サイト
# CSRF_TRUSTED_ORIGINS = ['https://your-domain.com']





