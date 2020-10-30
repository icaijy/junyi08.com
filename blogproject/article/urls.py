from django.urls import path

app_name = 'article'
from . import views

urlpatterns = [
    path('helloworld',views.helloworld, name='helloworld')
]