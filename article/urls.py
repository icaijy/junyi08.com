from django.urls import path

app_name = 'article'
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>/', views.detail, name='detail'),
    # path('visitor/', views.visitor, name='visitor'),
]