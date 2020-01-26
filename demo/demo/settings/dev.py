try:
    from .base import *
except ImportError:
    pass

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q3ezu@c)+8ajf^y4jtwupl@mf_g9^bsx0qxt1+d&+azebnpz*4'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# 网站标题
SITE_TITLE = '管理后台-DEV'
