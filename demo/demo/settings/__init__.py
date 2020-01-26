# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG is True:
    from .dev import *
else:
    from .production import *

MANAGE_NAME = 'admin'

MANAGE_PAGE = '/admin/service/article/'
