import xadmin
from datetime import datetime
from xadmin.views import CommAdminView, LoginView, filter_hook
from common import LOGIN_TITLE, BACKGROUND_INDEX
from . import sitemenu


class GlobalSetting(CommAdminView):
    menu_style = 'accordion'
    site_title = LOGIN_TITLE

    def get_site_menu(self):
        """
        网站侧边栏菜单
        :return:
        """
        site_menu = sitemenu.get_bar_menu(self)

        if self.user.is_superuser:
            return site_menu

        finial_menu = []
        for index, menus in enumerate(site_menu):
            main_menu = {}

            for index_menu, menu in enumerate(menus['menus']):
                if self.show_model_perm(menu):
                    if 'title' not in main_menu:
                        main_menu.update(
                            {'title': menus['title'], 'icon': menus['icon'], 'perm': menus['perm'], 'menus': []})
                    main_menu['menus'].append(menu)

            if main_menu:
                finial_menu.append(main_menu)

        return finial_menu

    def show_model_perm(self, menu):
        """
        是否在侧边栏展示
        :param menu:
        :return:
        """
        view_perm = 'model' in menu and self.user.has_perm(
            '%s.view_%s' % (menu['model']._meta.app_label, menu['model']._meta.model_name))

        show_perm = self.user.has_perm('%s.show_%s' % (menu['model']._meta.app_label, menu['model']._meta.model_name))
        hide_perm = self.user.has_perm('%s.hide_%s' % (menu['model']._meta.app_label, menu['model']._meta.model_name))

        return view_perm if show_perm else view_perm and not hide_perm

    @filter_hook
    def get_context(self):
        context = super(GlobalSetting, self).get_context()

        context.update({
            'site_web': LOGIN_TITLE,
            'site_url': '/admin/',
            'date': datetime.now().year,
        })

        return context


class LoginViewAdmin(LoginView):
    title = LOGIN_TITLE

    @filter_hook
    def get_context(self):
        context = super(LoginViewAdmin, self).get_context()

        context.update({
            'bg_index': BACKGROUND_INDEX,
        })

        return context


xadmin.site.register(CommAdminView, GlobalSetting)
xadmin.site.register(LoginView, LoginViewAdmin)
