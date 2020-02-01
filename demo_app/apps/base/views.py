from urllib.parse import unquote
from django.conf import settings
from django.urls import reverse, is_valid_path
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required

User = get_user_model()


def get_site_info(request):
    """
    根据登录的用户获取网站标题
    :param request:
    :return:
    """
    return {'site_web': settings.SITE_TITLE, }


@csrf_exempt
@login_required(login_url='/%s/login/' % settings.SITE_NAME)
def set_homepage(request):
    """
    设置首页
    :param request:
    :return:
    """
    try:
        obj = User.objects.filter(id=request.user.id)
        data = unquote(request.body.decode('utf-8'))
        url_path = data.split('url_path=')[1]
        obj.update(home_page=url_path)
    except Exception as e:
        return JsonResponse({'errcode': -1, 'errmsg': str(e)})
    else:
        return JsonResponse({'errcode': 0, 'errmsg': 'ok'})


class ManageRedirectView(RedirectView):
    """管理页面重定向"""

    def get_redirect_url(self, *args, **kwargs):
        """
        重定向
        :param args:
        :param kwargs:
        :return:
        """
        if isinstance(self.request.user, AnonymousUser):
            return reverse('xadmin:login')

        self.url = self.request.user.home_page if is_valid_path(self.request.user.home_page) is True else self.url

        return super().get_redirect_url(*args, **kwargs)
