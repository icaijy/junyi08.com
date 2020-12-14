from django.shortcuts import render
from django import http
from . import models
import markdown

from datetime import timedelta

from django import forms
from django.shortcuts import render
from django.utils.timezone import now

from tracking.models import Visitor, Pageview
from tracking.settings import TRACK_PAGEVIEWS
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


def visitor(request):
    end_time = now()
    start_time = end_time - timedelta(days=7)
    defaults = {'start': start_time, 'end': end_time}

    form = DashboardForm(data=request.GET or defaults)
    if form.is_valid():
        start_time = form.cleaned_data['start']
        end_time = form.cleaned_data['end']

    # queries take `date` objects (for now)
    user_stats = Visitor.objects.user_stats(start_time, end_time)
    visitor_stats = Visitor.objects.stats(start_time, end_time)

    context = {
        'user_stats': user_stats,
        'visitor_stats': visitor_stats,
    }
    return render(request, 'about/visitors.html', context)

# Create your views here.