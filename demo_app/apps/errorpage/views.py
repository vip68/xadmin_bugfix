from datetime import datetime
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render


def get_error_page(status_code, message):
    """
    获取错误页面
    :param status_code:
    :param message:
    :return:
    """
    context = {
        'site_web': settings.SITE_TITLE,
        'site_url': reverse(settings.SITE_NAME),
        'status_code': status_code,
        'message': message,
        'date': datetime.now().year
    }
    return context


def bad_request(request, exception=None):
    context = get_error_page(400, '对不起，你要找的这个页面突然不见了。不过，放心，一切都在我的掌控之中，不会跑多远！')
    return render(request, 'error.html', context, status=400)


def permission_denied(request, exception=None):
    context = get_error_page(403, '对不起，你无权浏览此页面。不过，放心，一个鸡腿给管理员即可解决！')
    return render(request, 'error.html', context, status=403)


def page_not_found(request, exception=None):
    context = get_error_page(404, '对不起，你要找的这个页面突然不见了。不过，放心，一切都在我的掌控之中，不会跑多远！')
    return render(request, 'error.html', context, status=404)


def server_error(request, exception=None):
    context = get_error_page(500, '对不起，内部服务器开小差。不过，放心，一个鸡腿让管理员唤醒它！')
    return render(request, 'error.html', context, status=500)
