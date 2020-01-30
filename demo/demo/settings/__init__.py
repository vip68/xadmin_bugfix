# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG is True:
    from .dev import *
else:
    from .production import *

SITE_NAME = 'admin'

SITE_PAGE = '/%s/service/article/' % SITE_NAME
