from django.shortcuts import render
from django import http


# Create your views here.

def helloworld(request):
    return http.HttpResponse("hello,world!")