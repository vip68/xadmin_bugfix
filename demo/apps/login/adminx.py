import xadmin
from datetime import datetime
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render
from django.forms import ValidationError
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext as _
from django.http.response import HttpResponseRedirect
from xadmin.forms import AdminAuthenticationForm, ERROR_MESSAGE
from xadmin.views import LoginView, filter_hook

UserModel = get_user_model()


class PasswordLoginAuthenticationForm(AdminAuthenticationForm):
    """密码登录权限校验"""

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        message = ERROR_MESSAGE

        if username and password:
            self.user_cache = authenticate(
                username=username, password=password)
            if self.user_cache is None:
                if u'@' in username:
                    # Mistakenly entered e-mail address instead of username? Look it up.
                    try:
                        user = UserModel.objects.get(email=username)
                    except (UserModel.DoesNotExist, UserModel.MultipleObjectsReturned):
                        # Nothing to do here, moving along.
                        pass
                    else:
                        if user.check_password(password):
                            message = _("Your e-mail address is not your username."
                                        " Try '%s' instead.") % user.username
                raise ValidationError(message)
            elif not self.user_cache.is_active or not self.user_cache.is_staff or not self.user_cache.is_pwd_login:
                raise ValidationError(message)
        return self.cleaned_data


class LoginViewAdmin(LoginView):
    title = settings.SITE_TITLE
    login_form = PasswordLoginAuthenticationForm
    login_template = None

    @filter_hook
    def get_context(self):
        context = super(LoginViewAdmin, self).get_context()

        context.update({
            'bg_path': 'xadmin/img/background.jpg',
        })

        return context

    @never_cache
    def post(self, request, *args, **kwargs):
        view = self.get(request)

        # 登录成功，view 的类型是 HttpResponseRedirect
        # 用户名肯定是存在了，不然也不会成功登录，所以这里不用对用户是否存在做判断
        if isinstance(view, HttpResponseRedirect):
            return HttpResponseRedirect(reverse('admin'))

        username = request.POST.get('username')
        user_obj = UserModel.objects.filter(username=username).first()
        context = get_render_context(user_obj)

        return render(request, 'login_fail.html', context)


def get_render_context(user_obj=None, message=None, history_href=None):
    """
    获取渲染内容
    :param user_obj:
    :param message:
    :param history_href:
    :return:
    """
    context = {
        'site_web': settings.SITE_TITLE,
        'site_url': reverse('admin'),
        'date': datetime.now().year,
    }
    context.update({'wait_second': 0 if user_obj is None else 10})
    if message is not None:
        context.update({'message': message})
    if message is not None:
        context.update({'history_href': history_href})

    return context


xadmin.site.register(LoginView, LoginViewAdmin)
