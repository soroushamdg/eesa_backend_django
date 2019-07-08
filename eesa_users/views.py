from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import  User
from django.contrib import auth
# Create your views here.
from django.template import loader

def check_email_address(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False

def signup(request):
    template = loader.get_template('users_index.html')
    context = {

    }
    if request.method == 'post':
        if request.POST['InputPasswordSignup'] == request.POST['InputPasswordRetypeSignup']:
            if check_email_address(request.POST['InputEmailSignup']):
                try:
                    user = User.objects.get(username=request.POST['InputEmailSignup'])
                    context['error'] = 'کاربری با این ایمیل ثبت نام کرده است.'
                except:
                    #creating account
                    user = User.objects.create_user(request,username=request.POST['InputEmailSignup'],
                                                    email=request.POST['InputEmailSignup'],
                                                    password=request.POST['InputPasswordSignup'])

                    name = request.POST['InputNameSignup'],
                    student_number = request.POST['InputStudentNumberSignup']
                    auth.login(request, user)
                    context['message'] = 'ثبت نام با موفقیت انجام شد.'
            else:
                context['error'] = 'ایمیل نامعتبر است.'
    else:
        pass

    return HttpResponse(template.render(context, request))


def signin(request):
    template = loader.get_template('users_index.html')
    context = {

    }
    if request.method == 'post':
        user = auth.authenticate(username = request.POST['InputEmailLogin'],
                                 password = request.POST['InputPasswordLogin'])
        if user is not None:
            auth.login(request,user)
            context['message'] = 'ورود با موفقیت انجام شد.'
        else:
            context['error'] = 'نام کاربری یا رمز عبور اشتباه است.'
    else:
        pass

    return HttpResponse(template.render(context, request))

def signout(request):
    if request.method == 'post':
        auth.logout(request)
        return redirect('home')