from django.apps import AppConfig

CHAR_MIN_LENGTH = 32
CHAR_MID_LENGTH = 64
CHAR_MAX_LENGTH = 128
CHAR_BIG_LENGTH = 256
CHAR_LARGE_LENGTH = 512
CHAR_EXT_LENGTH = 1024
FLAG = ((True, '是'), (False, '否'))


class UserProfileConfig(AppConfig):
    name = 'users'
    verbose_name = '用户管理'


class BaseConfig(AppConfig):
    name = 'base'
    verbose_name = '基础配置'


class ServiceConfig(AppConfig):
    name = 'service'
    verbose_name = '服务大厅'
