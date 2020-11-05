from django.shortcuts import render
from django import http
from . import models

def articleList(request):
    articles = models.Article.objects.all()
    context = {'articles':articles}
    return render(request, 'article/list.html', context)

# Create your views here.