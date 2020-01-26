import xadmin
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model
from xadmin.layout import Main, Fieldset, Side, Row
from xadmin.plugins.auth import UserAdmin

from .models import UserProfile

User = get_user_model()


class UserProfileAdmin(UserAdmin):
    change_user_password_template = None
    form_layout = None
    list_display = ('username', 'zh_name', 'user_id', 'is_superuser', 'is_pwd_login', 'is_staff', 'is_active',
                    'home_page', 'last_login',)
    list_filter = ('is_staff', 'is_superuser', 'is_pwd_login', 'is_active', 'last_login')
    search_fields = ('username', 'zh_name', 'email')
    ordering = ('-is_superuser', '-is_pwd_login', 'user_id', 'last_login',)
    show_detail_fields = ('zh_name',)
    style_fields = {'user_permissions': 'm2m_transfer', 'groups': 'm2m_dropdown'}
    model_icon = 'fa fa-user'
    relfield_style = 'fk-ajax'

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'username', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset(_('Personal info'),
                             Row('zh_name', 'user_id'),
                             Row('email', 'home_page', ),
                             css_class='unsort'
                             ),
                    Fieldset(_('Permissions'),
                             'groups', 'user_permissions',
                             css_class='unsort'
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined',
                             css_class='unsort'
                             ),
                ),
                Side(
                    Fieldset(_('Status'),
                             'is_active', 'is_staff', 'is_pwd_login', 'is_superuser',
                             ),
                    css_class='unsort'
                )
            )
        return super(UserAdmin, self).get_form_layout()


xadmin.site.unregister(User)
xadmin.site.register(UserProfile, UserProfileAdmin)
