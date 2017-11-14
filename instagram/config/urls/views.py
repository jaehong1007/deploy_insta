from django.conf.urls import url, include
from django.contrib import admin

from .. import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Post application
    url(r'^post/', include('post.urls.views', namespace='post')),

    # Member application
    url(r'^members/', include('member.urls.views', namespace='member')),
    #
    # config
    url(r'^$', views.index, name='index'),
    ]
