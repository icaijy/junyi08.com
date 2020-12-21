from django.shortcuts import render
from django import http
from . import models
import markdown

from django.shortcuts import render
from django.utils.timezone import now

def articleList(request):
    articles = models.Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'index.html', context)


def detail(request, id):
    try:
        article = models.Article.objects.get(id=id)
        article.views += 1
        article.save(update_fields=['views'])
        article.content = markdown.markdown(article.content,extensions=['markdown.extensions.extra','markdown.extensions.codehilite','markdown.extensions.toc'])
        context = {
            'article':article,
        }
    except:
        raise http.Http404
    return render(request, 'article/detail.html', context)


# visitor count
from django import forms
from tracking.models import Visitor
from datetime import timedelta

input_formats = [
    '%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M',       # '2006-10-25 14:30'
    '%Y-%m-%d',             # '2006-10-25'
    '%Y-%m',                # '2006-10'
    '%Y',                   # '2006'
]
class DashboardForm(forms.Form):
    start = forms.DateTimeField(required=False, input_formats=input_formats)
    end = forms.DateTimeField(required=False, input_formats=input_formats)

def visitor(request):
    week_total = []
    week_unique = []
    end_time = now()
    # start time: track start time
    start_time = Visitor.objects.order_by('start_time')[0].start_time
    visitor_stats = Visitor.objects.stats(start_time, end_time)

    for x in range(7):
        week_total.append(Visitor.objects.stats(\
            end_time-timedelta(days=x+1), \
            end_time-timedelta(days=x))['total'])

    for x in range(7):
        week_unique.append(Visitor.objects.stats(\
            end_time-timedelta(days=x+1), \
            end_time-timedelta(days=x))['unique'])

    context = {
        'visitor_stats': visitor_stats,
        'week_total':week_total,
        'week_unique':week_unique
    }
    return render(request, 'about/visitors.html', context)

# Create your views here.