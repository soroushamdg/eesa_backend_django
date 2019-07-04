from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from eesa_courses.models import courses_course
from eesa_main.models import eesa_team_member


def last_courses(number):
    posts = list()
    if number < courses_course.objects.count():
        for i in range(number):
            posts.append(courses_course.objects.all().reverse()[courses_course.objects.count()-i])
    else:
        posts = courses_course.objects.all()
    return posts


def last_crew(number):
    posts = list()
    if number < eesa_team_member.objects.count():
        for i in range(number):
            posts.append(eesa_team_member.objects.all().reverse()[eesa_team_member.objects.count()-i])
    else:
        posts = eesa_team_member.objects.all()
    return posts


def index(request):
    template = loader.get_template('eesa_index.html')
    context = {
        'page_url' : 'home',
        'courses' : last_courses(5),
        'team_members' : last_crew(5),
        'all_team' : eesa_team_member.objects.all()
    }
    return HttpResponse(template.render(context,request))

