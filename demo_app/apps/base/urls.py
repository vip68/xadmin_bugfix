from django.urls import path
from base.views import set_homepage

app_name = 'base'

urlpatterns = [
    path('homepage', set_homepage, name='homepage'),
]
