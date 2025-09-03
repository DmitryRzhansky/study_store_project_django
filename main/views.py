from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная',
        'content': 'Главная страница магазина'
    }

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('Страница о нас')