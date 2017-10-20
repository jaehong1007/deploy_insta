from django.contrib.auth import logout as django_logout, login as django_login
from django.http import HttpResponse

from django.shortcuts import render, redirect

from .forms import SignupForm, LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('post:post_list')
        else:
            return HttpResponse('Login credential invalid')
    else:
        form = LoginForm()
    context = {
        'login_form': form
    }
    return render(request, 'member/login.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.signup()
            django_login(request, user)
            return redirect('post:post_list')
        # return HttpResponse(f'{user.username}, {user.password}')
    else:
        form = SignupForm
    context = {
        'signup_form': form,
    }
    return render(request, 'member/signup.html', context)


def logout(request):
    django_logout(request)
    return redirect('post:post_list')
