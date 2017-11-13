from django.conf.urls import url

from member import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='signin'),
    url(r'^logout/$', views.logout, name='signout'),
    url(r'^profile/(?P<user_pk>\d+)/$', views.profile, name='profile'),
    url(r'^facebook-login/$', views.facebook_login, name='facebook_login'),
    url(r'^follow/(?P<user_pk>\d+)/$', views.follow_toggle, name='follow_toggle'),
    url(r'^front-facebook-login/$', views.FrontFacebookLogin.as_view(), name='front-facebook-login'),
]
