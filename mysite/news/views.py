from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def index(request):
    return HttpResponse('<h1>Тут будет блок с новостями</h1>')


def main(request):
    context = {
        'title': 'Новости',
        'news': News.objects.all(),
        'comments': Comments.objects.all(),
        'category': Category.objects.all()
    }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    context = {
        'title': 'Новости',
        'news': News.objects.filter(category_id=category_id),
        'comments': Comments.objects.all(),
        'category': Category.objects.all()
    }
    return render(request, 'news/index.html', context)