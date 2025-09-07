from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    context = {
        'title': 'Главная',
        'content': 'Магазин обуви rzh_exe',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'Магазин обуви rzh_exe',
        'text_on_page': 'Магазин для продажи обуви'
    }

    return render(request, 'main/about.html', context)