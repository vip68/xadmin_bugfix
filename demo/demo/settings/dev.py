try:
    from .base import *
except ImportError:
    pass

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q3ezu@c)+8ajf^y4jtwupl@mf_g9^bsx0qxt1+d&+azebnpz*4'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.mysql',
        # 'USER': 'root',
        # 'PASSWORD': '123456',
        # 'NAME': 'demo',
        # 'HOST': '127.0.0.1',
        # 'PORT': '3306',
        # 'OPTIONS': {
        #     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'; SET NAMES utf8mb4;"
        # }
    }
}

# 网站标题
SITE_TITLE = '管理后台-DEV'
