from datetime import datetime
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render


def index_view(request):
    context = {
        'date': datetime.now().year,
        'site_url': reverse(settings.SITE_NAME),
    }
    return render(request, 'xadmin/views/index.html', context)
