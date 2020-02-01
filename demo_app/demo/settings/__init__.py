from .base import *

DEBUG = True

if DEBUG is True:
    from .dev import *
else:
    from .production import *

# 站点名称
SITE_NAME = 'manage'

# 后台首页
SITE_PAGE = '/%s/service/article/' % SITE_NAME
