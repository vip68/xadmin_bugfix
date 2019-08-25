from django.db import models

from apps import CHAR_MIN_LENGTH


class UrlsLink(models.Model):
    name = models.CharField(verbose_name='名称', max_length=CHAR_MIN_LENGTH, default=True, null=True)

    class Meta:
        verbose_name = '超级链接'
        verbose_name_plural = '超级链接'


class AppUrlLink(UrlsLink):
    class Meta:
        verbose_name = '快捷访问'
        verbose_name_plural = '快捷访问'
        proxy = True
