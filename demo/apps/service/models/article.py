from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    ARTICLE_TYPE = (
        (0, 'BUG反馈'),
        (1, '意见建议'),
        (2, '讨论'),
        (3, '技术'),
        (4, '帮助'),
        (5, '公告'),
    )
    category = models.PositiveSmallIntegerField(verbose_name='主题分类', choices=ARTICLE_TYPE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='发布者', on_delete=models.CASCADE, null=True)
    publish_time = models.DateTimeField(verbose_name='发帖时间', auto_now_add=True, null=True)
    update_time = models.DateTimeField(verbose_name='更新时间', blank=True, null=True)
    view_count = models.PositiveSmallIntegerField(verbose_name='浏览次数', default=0)
    title = models.CharField(verbose_name='主题', max_length=30, help_text='字数限制在30个字以内')
    content = RichTextUploadingField(verbose_name='内容')

    class Meta:
        verbose_name = '畅所欲言'
        verbose_name_plural = '畅所欲言'

    def __str__(self):
        return str(self.title)


class ReleaseLog(Article):
    class Meta:
        verbose_name = '服务大厅'
        verbose_name_plural = '服务大厅'
        proxy = True
