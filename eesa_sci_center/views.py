from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import loader

from eesa_main.models import eesa_information
from eesa_sci_center.models import scicenter_category, scicenter_writer, scicenter_tutorial, scicenter_document, \
    scicenter_project
import datetime
# Create your views here.
def last_tag_items(number):
    if number < scicenter_category.objects.count():
        return scicenter_category.objects.all().order_by('-id')[0:-number]
    else:
        return scicenter_category.objects.all()

def last_pub_items(number):
    if number < scicenter_writer.objects.count():
        return scicenter_writer.objects.all().order_by('-id')[0:-number]
    else:
        return scicenter_writer.objects.all()

def last_tutorial_items(number):
    if number < scicenter_tutorial.objects.count():
        return scicenter_tutorial.objects.all().order_by('-id')[0:-number]
    else:
        return scicenter_tutorial.objects.all()


def last_document_items(number):
    if number < scicenter_document.objects.count():
        return scicenter_document.objects.all().order_by('-id')[0:-number]
    else:
        return scicenter_document.objects.all()


def last_project_items(number):
    if number < scicenter_project.objects.count():
        return scicenter_project.objects.all().order_by('-id')[0:-number]
    else:
        return scicenter_project.objects.all()


@login_required
def index(request):
    template = loader.get_template('scicenter_index')

    context= {
        'all_tags': scicenter_category.objects.order_by('name'),
        'all_pubs': scicenter_writer.objects.order_by('name'),
        'all_tutorials' : last_tutorial_items(25),
        'all_documents': last_document_items(25),
        'all_projects': last_project_items(25),
        'eesa_information': eesa_information.objects.last(),

    }
    return HttpResponse(template.render(context,request))

@login_required
def category_index(request, cat_id):
    template = loader.get_template('scicenter_index')
    context = {
        'all_tags': scicenter_category.objects.order_by('name'),
        'all_pubs': scicenter_writer.objects.order_by('name'),
        'all_tutorials': None,
        'all_documents': None,
        'all_projects': None,
        'eesa_information': eesa_information.objects.last(),

    }
    #GET TUTORIALS
    try:
        context['all_tutorials'] = get_list_or_404(scicenter_tutorial, category__pk=cat_id)
    except:
        context['all_tutorials'] = None

    #GET DOCUMENTS
    try:
        context['all_documents'] = get_list_or_404(scicenter_document, category__pk=cat_id)
    except:
        context['all_documents'] = None

    #GET PROJECTS
    try:
        context['all_projects'] = get_list_or_404(scicenter_project, category__pk=cat_id)
    except:
        context['all_projects'] = None

    return HttpResponse(template.render(context, request))


@login_required
def publisher_index(request, pub_id):
    template = loader.get_template('scicenter_index')
    context = {
        'all_tags': scicenter_category.objects.order_by('name'),
        'all_pubs': scicenter_writer.objects.order_by('name'),
        'all_tutorials': None,
        'all_documents': None,
        'all_projects': None,
        'eesa_information': eesa_information.objects.last(),

    }
    # GET TUTORIALS
    try:
        context['all_tutorials'] = get_list_or_404(scicenter_tutorial, writer__pk=pub_id)
    except:
        context['all_tutorials'] = None

    # GET DOCUMENTS
    try:
        context['all_documents'] = get_list_or_404(scicenter_document, writer__pk=pub_id)
    except:
        context['all_documents'] = None

    # GET PROJECTS
    try:
        context['all_projects'] = get_list_or_404(scicenter_project, writer__pk=pub_id)
    except:
        context['all_projects'] = None

    return HttpResponse(template.render(context, request))


@login_required
def search_index(request):
    template = loader.get_template('scicenter_index')
    find_query = request.GET.get('scisch')
    print(find_query)
    context = {
        'all_tags': scicenter_category.objects.order_by('name'),
        'all_pubs': scicenter_writer.objects.order_by('name'),
        'all_tutorials': None,
        'all_documents': None,
        'all_projects': None,
        'eesa_information': eesa_information.objects.last(),

    }

    context['all_tutorials'] = scicenter_tutorial.objects.filter(Q(name__icontains = find_query))
    context['all_documents'] = scicenter_document.objects.filter(Q(name__icontains = find_query))
    context['all_projects'] = scicenter_project.objects.filter(Q(name__icontains = find_query))
    return HttpResponse(template.render(context, request))