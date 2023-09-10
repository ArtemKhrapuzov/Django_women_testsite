from django.http import HttpResponse
from django.shortcuts import render

from .models import Women

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts})

def categories(request, catid):
    context = {
        'catid': catid
    }
    return render(request, 'women/about.html', context=context)
