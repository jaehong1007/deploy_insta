from django.conf.urls import url

from member import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='signin'),
    url(r'^logout/$', views.logout, name='signout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^facebook-login/$', views.facebook_login, name='facebook_login'),
]
