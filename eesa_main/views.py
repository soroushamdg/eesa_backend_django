from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('web site is up!;p')

def wtf(request):
    return HttpResponse('wtf?!')