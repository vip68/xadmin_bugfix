from xadmin.adminx import Log
from reversion.models import Revision
from xadmin.plugins.auth import Permission, Group
from users.models import UserProfile
from service.models import Article, AppUrlLink


def get_bar_menu(self):
    """
    侧边栏菜单
    :param self:
    :return:
    """
    return [
        {'title': '服务大厅', 'icon': 'fa fa-send', 'perm': self.get_model_perm(Article, 'change'),
         'menus': [
             {'model': Article, 'title': '畅所欲言', 'icon': 'fa fa-microphone',
              'url': self.get_model_url(Article, 'changelist')},
         ]},
        {'title': '快捷访问', 'icon': 'fa fa-external-link-square', 'perm': self.get_model_perm(Article, 'view'),
         'menus': [
             {'model': AppUrlLink, 'title': '纵世科技', 'icon': 'fa fa-bar-chart', 'blank': True,
              'url': 'https://v88v.cnblogs.com'},
         ]},
        {'title': '系统管理', 'icon': 'fa fa-cogs', 'perm': self.get_model_perm(Article, 'change'),
         'menus': [
             {'model': Revision, 'title': '版本回溯', 'icon': 'fa-fw fa fa-exchange',
              'url': self.get_model_url(Revision, 'changelist')},
             {'model': Log, 'title': '操作日志', 'icon': 'fa-fw fa fa-cog',
              'url': self.get_model_url(Log, 'changelist')},
         ]},
        {'title': '认证和授权', 'icon': 'fa-fw fa fa-group', 'perm': self.get_model_perm(Article, 'view'),
         'menus': [
             {'model': Group, 'title': '组', 'icon': 'fa-fw fa fa-group',
              'url': self.get_model_url(Group, 'changelist')},
             {'model': UserProfile, 'title': '用户', 'icon': 'fa-fw fa fa-user',
              'url': self.get_model_url(UserProfile, 'changelist')},
             {'model': Permission, 'title': '权限', 'icon': 'fa-fw fa fa-lock',
              'url': self.get_model_url(Permission, 'changelist')},
         ]},
    ]
