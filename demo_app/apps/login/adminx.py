from django.conf import settings
from django.urls import reverse, is_valid_path
from django.forms import ValidationError
from django.contrib.auth import get_user_model
from django.http.response import HttpResponseRedirect
from django.views.decorators.cache import never_cache
from xadmin import site
from xadmin.forms import AdminAuthenticationForm
from xadmin.views import LoginView, filter_hook

User = get_user_model()


class PasswordLoginAuthenticationForm(AdminAuthenticationForm):
    """密码登录权限校验"""

    def clean(self):
        cleaned_data = super().clean()
        if self.user_cache is not None and not self.user_cache.is_pwd_login:
            raise ValidationError('帐号密码登录方式已停用，请使用钉钉扫码登录！')

        return cleaned_data


class LoginViewAdmin(LoginView):
    title = settings.SITE_TITLE
    login_form = PasswordLoginAuthenticationForm

    @filter_hook
    def get_context(self):
        context = super(LoginViewAdmin, self).get_context()

        context.update({
            'site_web': settings.SITE_TITLE,
            'bg_path': settings.LOGIN_BG_IMG,
        })

        return context

    @never_cache
    def post(self, request, *args, **kwargs):
        view = self.get(request)

        # 登录成功，view 的类型是 HttpResponseRedirect
        # 帐号登录方式的用户名肯定是存在了，不然也不会成功登录，所以这里不用对用户是否存在做判断
        if isinstance(view, HttpResponseRedirect):
            # 如果当前就是登录页，那么就不要跳到登录页
            url_path = request.path if is_valid_path(request.path) is True and request.path != reverse(
                'xadmin:login') else reverse(settings.SITE_NAME)
            return HttpResponseRedirect(url_path)

        return view


site.register(LoginView, LoginViewAdmin)
