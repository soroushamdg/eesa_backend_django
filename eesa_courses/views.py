from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def courses_index(request):
    return HttpResponse('website is up and running!:p')