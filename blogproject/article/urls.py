from django.urls import path

app_name = 'article'
from . import views

urlpatterns = [
    path('articleList/', views.articleList, name='articleList')
]