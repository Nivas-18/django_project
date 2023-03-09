from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def First(request):
    return HttpResponse('<h1><marquee>My name is nivas</marquee></h1>')