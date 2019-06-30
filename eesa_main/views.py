from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def index(request):
    template = loader.get_template('eesa_index.html')
    context = {
        'page_url' : 'home'
    }
    return HttpResponse(template.render(context,request))

