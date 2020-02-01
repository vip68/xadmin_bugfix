"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.conf import settings
from django.urls import path, include
from django.views.generic.base import RedirectView
from xadmin.plugins import xversion
from index.views import index_view
from base.views import ManageRedirectView

xadmin.autodiscover()
xversion.register_models()

work_urlpatterns = [
    path('', ManageRedirectView.as_view(url=settings.SITE_PAGE), name=settings.SITE_NAME),
    path('', xadmin.site.urls),
    path('base/', include('base.urls')),
]

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/xadmin/img/favicon.ico')),
    path('', index_view, name='index'),
    path('%s/' % settings.SITE_NAME, include(work_urlpatterns)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

handler400 = 'errorpage.views.bad_request'
handler403 = 'errorpage.views.permission_denied'
handler404 = 'errorpage.views.page_not_found'
handler500 = 'errorpage.views.server_error'

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
