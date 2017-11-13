"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from config.views import index
from member.apis import Login
from post.apis import PostList, PostDetail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Post application
    url(r'^post/', include('post.urls', namespace='post')),

    # Member application
    url(r'^members/', include('member.urls', namespace='member')),
    #
    # config
    url(r'^$', index, name='index'),
    # api
    url(r'^api/post/$', PostList.as_view(), name='api-post'),
    url(r'^api/post/(?P<user_pk>\d+)/$', PostDetail.as_view(), name='api-post-detail'),
    url(r'^api/member/login/$', Login.as_view(), name='api-login')
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
