from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.
from django.template import loader

from eesa_courses.models import courses_course
from eesa_main.models import eesa_information

@login_required
def courses_index(request):
    template = loader.get_template('courses_index.html')

    context = {
        'page_url': 'courses',
        'eesa_information': eesa_information.objects.last(),
        'courses' : courses_course.objects.all()
    }
    return HttpResponse(template.render(context, request))

def courses_search(request):
    template = loader.get_template('courses_index.html')
    find_query = request.GET.get('crsch')
    context = {
        'page_url': 'courses',
        'eesa_information': eesa_information.objects.last(),
        'courses': courses_course.objects.filter(Q(name__icontains = find_query))
    }
    return HttpResponse(template.render(context, request))