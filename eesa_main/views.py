from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from eesa_courses.models import courses_course


def last_courses(number):
    posts = list()
    if number < courses_course.objects.count():
        for i in range(number):
            posts.append(courses_course.objects.all().reverse()[courses_course.objects.count()-i])
    else:
        posts = courses_course.objects.all()
    return posts

def index(request):
    template = loader.get_template('eesa_index.html')
    context = {
        'page_url' : 'home',
        'courses' : last_courses(5)
    }
    return HttpResponse(template.render(context,request))

