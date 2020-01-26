from datetime import datetime
from django.shortcuts import render


def index_view(request):
    return render(request, 'xadmin/views/index.html', {'date': datetime.now().year})
