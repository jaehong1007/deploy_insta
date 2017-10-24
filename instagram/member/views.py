from pprint import pprint
from typing import NamedTuple

import requests
from django.contrib.auth import logout as django_logout, login as django_login, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.urls import reverse

from config import settings
from config.settings import FACEBOOK_APP_ID
from .forms import LoginForm, SignUpForm

User = get_user_model()


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
        'facebook_app_id': settings.FACEBOOK_APP_ID,
        'scope': settings.FACEBOOK_SCOPE,
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


@login_required
def profile(request):
    return HttpResponse(f'User profile page {request.user}')


def facebook_login(request):
    class AccessTokenInfo(NamedTuple):
        access_token: str
        token_type: str
        expires_in: str

    class DebugTokenInfo(NamedTuple):
        app_id: str
        application: str
        expires_at: int
        is_valid: bool
        issued_at: int
        scopes: list
        type: str
        user_id: str

    app_id = settings.FACEBOOK_APP_ID
    app_secret_code = settings.FACEBOOK_SECRET_CODE
    app_access_token = f'{app_id}|{app_secret_code}'
    code = request.GET.get('code')

    def get_access_token_info(code):

        redirect_uri = '{scheme}://{host}{relative_url}'.format(
            scheme=request.scheme,
            host=request.META['HTTP_HOST'],
            relative_url=reverse('member:facebook_login'),
        )
        print('redirect_uri:', redirect_uri)
        url_access_token = 'https://graph.facebook.com/v2.10/oauth/access_token'
        params_access_token = {
            'client_id': app_id,
            'redirect_uri': redirect_uri,
            'client_secret': app_secret_code,
            'code': code,
        }
        response = requests.get(url_access_token, params_access_token)

        return AccessTokenInfo(**response.json())

    def get_debug_token_info(token):
        url_debug_token = 'https://graph.facebook.com/debug_token'
        params_debug_token = {
            'input_token': access_token,
            'access_token': app_access_token,
        }
        response = requests.get(url_debug_token, params_debug_token)
        return DebugTokenInfo(**response.json()['data'])

    access_token_info = get_access_token_info(code)

    access_token = access_token_info.access_token

    debug_token_info = get_debug_token_info(access_token)

    user_info_fields = {
        'id',
        'name',
        'picture',
        'email',
    }
    url_graph_user_info = 'https://graph.facebook.com/me'
    params_graph_user_info = {
        'fields': ','.join(user_info_fields),
        'access_token': access_token,
    }
    response = requests.get(url_graph_user_info, params_graph_user_info)
    result = response.json()
    return HttpResponse(result.items())
    # return HttpResponse(debug_token_info)



