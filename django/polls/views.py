from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("dockerでdjangoの環境構築できた！")
