from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Women, Category

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
]

def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'cats': cats,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html')


def addpage(request):
    return HttpResponse('добавить')

def contact(request):
    return HttpResponse('контакты')

def login(request):
    return HttpResponse('логин')

def show_post(request, post_id):
    post = Women.objects.get(id=post_id)
    return HttpResponse(f'post {post_id}')

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'cats': cats,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)