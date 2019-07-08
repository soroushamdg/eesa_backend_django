from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import  User
from django.contrib import auth
# Create your views here.
from django.template import loader

from eesa_users.models import user_student


def check_email_address(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False

def signup(request):
    template = loader.get_template('users_index.html')
    context = {

    }
    if request.method == 'POST':
        if request.POST['InputPasswordSignup'] == request.POST['InputPasswordRetypeSignup']:
            if check_email_address(request.POST['InputEmailSignup']):
                try:
                    user = User.objects.get(username=request.POST['InputEmailSignup'])
                    context['error'] = 'کاربری با این ایمیل ثبت نام کرده است.'
                except User.DoesNotExist:
                    #creating account
                    user_account = User.objects.create_user(username=request.POST['InputEmailSignup'],email=request.POST['InputEmailSignup'],password=request.POST['InputPasswordSignup'])

                    student = user_student(user=user_account,
                                           name = request.POST['InputNameSignup'],
                                           student_number = request.POST['InputStudentNumberSignup'])
                    user_account.save()
                    student.save()
                    auth.login(request, user_account)
                    context['error'] = 'ثبت نام با موفقیت انجام شد.'
                    return redirect('home')
            else:
                context['error'] = 'ایمیل نامعتبر است.'
    else:
        pass

    return HttpResponse(template.render(context, request))


def signin(request):
    template = loader.get_template('users_index.html')
    context = {

    }
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['InputEmailLogin'],
                                 password = request.POST['InputPasswordLogin'])
        print(user)
        if user is not None:
            auth.login(request,user = user)
            context['error'] = 'ورود با موفقیت انجام شد.'
            print(context)
            return redirect('home')
        else:
            context['error'] = 'نام کاربری یا رمز عبور اشتباه است.'
            print(context)
            return HttpResponse(template.render(context, request))
    else:
        pass
    print(context)
    return HttpResponse(template.render(context, request))

def signout(request):
    auth.logout(request)
    return redirect('home')