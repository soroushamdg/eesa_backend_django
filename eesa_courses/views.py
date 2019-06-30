from django.http import HttpResponse

# Create your views here.
from django.template import loader

from eesa_courses.models import courses_course


def courses_index(request):
    template = loader.get_template('courses_index.html')

    context = {
        'page_url': 'courses',
        'courses' : courses_course.objects.all()
    }
    return HttpResponse(template.render(context, request))