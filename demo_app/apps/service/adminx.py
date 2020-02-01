import xadmin
import datetime
from django.conf import settings
from django.contrib.auth import get_permission_codename
from xadmin.sites import site
from xadmin.views import filter_hook, ModelAdminView, DetailAdminView
from xadmin.layout import Main, Field
from .models import Article, ReleaseLog


class ArticleAdmin(ModelAdminView):
    hidden_menu = True
    form_layout = None
    list_display = ('category', 'title', 'user', 'publish_time', 'update_time', 'view_count',)
    list_display_links = ('title',)
    search_fields = ('title', 'user__first_name',)
    list_filter = ('publish_time', 'update_time',)
    exclude = ('user', 'update_time', 'view_count',)
    model_icon = 'fa fa-microphone'
    reversion_enable = True
    aggregate_fields = {'view_count': 'sum',}

    def get_form_layout(self):
        self.form_layout = (
            Main(
                'category',
                Field('title', css_class="extra"),
                'content',
            ),
        )
        return super(ArticleAdmin, self).get_form_layout()

    def save_models(self):
        self.new_obj.user = self.request.user
        if self.new_obj.publish_time is not None:
            self.new_obj.update_time = datetime.datetime.now()
        self.new_obj.save()

        super().save_models()

    def get_model_perms(self):
        perms = super(ArticleAdmin, self).get_model_perms()
        perms.update({'view': self.has_view_article_permission()})
        return perms

    def has_view_article_permission(self):
        codename = get_permission_codename('view', self.opts)
        return ('view' not in self.remove_permissions) and self.user.has_perm('%s.%s' % (self.app_label, codename))

    @filter_hook
    def get_object_url(self, obj):
        # 只要到view界面，不需要到编辑页面或者详情页面，因为设定要先进入view页面之后再去选择编辑
        if self.has_view_article_permission():
            return self.model_admin_url("view", getattr(obj, self.opts.pk.attname))
        else:
            return None

    @filter_hook
    def get_context(self):
        context = super(ArticleAdmin, self).get_context()
        # 限制提示信息只在首页列表页出现
        if not (self.request.path.endswith('/update/') or self.request.path.endswith(
                '/add/') or self.request.path.endswith('/delete/') or hasattr(self, 'model_perm')):
            context.update({
                'welcome_msg': '欢迎大家在此留言，提出宝贵意见和建议，大家携手共同进步！',
                'alert_type': 'success',
            })

        return context


class BaseHelperAdmin(DetailAdminView):
    hidden_menu = True
    article_obj = None
    has_modify_permission = False
    has_del_permission = False
    object_list_template = 'xadmin/views/article_detail.html'
    detail_template = 'xadmin/views/article_detail.html'

    def init_request(self, object_id, *args, **kwargs):
        super(BaseHelperAdmin, self).init_request(object_id, *args, **kwargs)

        # 限制普通用户只能编辑自己的帖子，无法删帖
        if self.user.is_superuser:
            self.has_modify_permission = True
            self.has_del_permission = True
        elif self.user == self.obj.user:
            self.has_modify_permission = True

        # 浏览次数自增1
        self.org_obj.view_count += 1
        self.org_obj.save()

    @filter_hook
    def get_context(self):
        context = super(BaseHelperAdmin, self).get_context()

        try:
            article_title = self.article_obj.title
            publisher = self.article_obj.user
            publish_time = self.article_obj.publish_time
            update_time = self.article_obj.update_time
            content = self.article_obj.content
            view_count = self.org_obj.view_count
        except Exception as e:
            article_title = '指定的主题不存在'
            content = str(e),
            publisher = ''
            publish_time = ''
            update_time = ''
            view_count = 0

        context.update({
            'article_title': article_title,
            'publisher': publisher,
            'publish_time': publish_time,
            'update_time': update_time,
            'view_count': view_count,
            'content': content,
            'app_label': self.app_label,
            'brand_name': self.opts.verbose_name_plural,
            'brand_icon': self.get_model_icon(self.model),
            'opts_url': '/%s/service/article/' % settings.SITE_NAME,
            'has_change_permission': context['has_change_permission'] and self.has_modify_permission,
            'has_delete_permission': context['has_delete_permission'] and self.has_del_permission,
            'has_view_article_permission': self.has_view_article_permission(),
        })

        return context

    def has_view_article_permission(self):
        codename = get_permission_codename('view', self.opts)
        return ('view' not in self.remove_permissions) and self.user.has_perm('%s.%s' % (self.app_label, codename))


class ViewArticleAdmin(BaseHelperAdmin):
    @filter_hook
    def get_context(self):
        try:
            self.article_obj = Article.objects.get(id=int(self.args[0]))
        except Exception as e:
            print(e)
            self.article_obj = None

        return super(ViewArticleAdmin, self).get_context()


class ReleaseLogAdmin(BaseHelperAdmin):
    @filter_hook
    def get_context(self):
        index = 1
        try:
            self.article_obj = Article.objects.get(id=index)
        except Exception as e:
            print(e)
            self.article_obj = None

        context = super(ReleaseLogAdmin, self).get_context()
        context.update({
            'edit_url': '/%s/service/article/%d/update' % (settings.SITE_NAME, index),
            'delete_url': '/%s/service/article/%d/delete' % (settings.SITE_NAME, index),
        })

        return context


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(ReleaseLog, ReleaseLogAdmin)

site.register_modelview(r'^(.+)/view/$', ViewArticleAdmin, name='%s_%s_view')
