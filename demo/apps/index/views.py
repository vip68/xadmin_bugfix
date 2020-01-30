from datetime import datetime
from django.shortcuts import render
from django.conf import settings


def index_view(request):
    context = {
        'date': datetime.now().year,
        'site_path': '/%s/' % settings.SITE_NAME
    }
    return render(request, 'xadmin/views/index.html', context)
