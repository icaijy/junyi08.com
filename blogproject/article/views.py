from django.shortcuts import render
from django import http
from . import models

def articleList(request):
    articles = models.Article.objects.all()
    context = {'articles' : articles}
    return render(request, 'article/index.html', context)

def detail(request, id):
    article = models.Article.objects.get(id=id)
    context = {'article':article}
    return render(request, 'article/detail.html', context)

# Create your views here.