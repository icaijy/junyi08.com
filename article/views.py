from django.shortcuts import render
from django import http
from . import models
import markdown

from django.shortcuts import render
from django.utils.timezone import now

def index(request):
    articles = models.Article.objects.all()
    hot = articles.order_by('-pin','-views')
    new = articles.order_by('-createTime')
    context = {
        'hot' : hot,
        'newest':new
    }
    return render(request, 'index.html', context)


def detail(request, id):
    try:
        article = models.Article.objects.get(id=id)
        article.views += 1    # views +1
        article.save(update_fields=['views'])    # save to database
        md = markdown.Markdown(article.content,extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        article.content = md.convert(article.content)
        context = {
            'article':article,
            'toc':md.toc
        }
    # if article not found
    except models.Article.DoesNotExist:
        raise http.Http404
    return render(request, 'article/detail.html', context)

# Create your views here.