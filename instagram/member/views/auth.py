
from django.contrib.auth import logout as django_logout, login as django_login, get_user_model
from django.http import HttpResponse

from django.shortcuts import render, redirect


from config.settings.dev import FACEBOOK_APP_ID, FACEBOOK_SCOPE
from ..forms import LoginForm, SignUpForm

User = get_user_model()

__all__ = (
    'login',
    'signup',
    'logout',
)


def login(request):
    next_path = request.GET.get('next')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            if next_path:
                return redirect(next_path)
            return redirect('post:post_list')
        else:
            return HttpResponse('Login credential invalid')
    else:
        form = LoginForm()
    context = {
        'login_form': form,
        'facebook_app_id': FACEBOOK_APP_ID,
        'scope': FACEBOOK_SCOPE,
    }
    return render(request, 'member/login.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            django_login(request, user)
            return redirect('post:post_list')
        # return HttpResponse(f'{user.username}, {user.password}')
    else:
        form = SignUpForm
    context = {
        'signup_form': form,
    }
    return render(request, 'member/signup.html', context)


def logout(request):
    django_logout(request)
    return redirect('post:post_list')