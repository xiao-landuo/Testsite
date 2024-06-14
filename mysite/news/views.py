from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #print(dir(request))
    return HttpResponse('Hellow world')

def test(request):
    #print(dir(request))
    return HttpResponse('<h1>Тестовая страница</h1>')