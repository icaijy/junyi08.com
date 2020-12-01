from django.shortcuts import render
from django import http
from . import models
import markdown


def articleList(request):
    articles = models.Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'index.html', context)

def detail(request, id):
    article = models.Article.objects.get(id=id)
    article.content = markdown.markdown(article.content,extensions=['markdown.extensions.extra','markdown.extensions.codehilite','markdown.extensions.toc'])
    context = {
        'article':article,
    }
    return render(request, 'article/detail.html', context)

# Create your views here.