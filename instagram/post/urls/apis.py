from django.conf.urls import url

from ..apis import PostList, PostDetail

urlpatterns = [
    url(r'^post/$', PostList.as_view(), name='post-list'),
    url(r'^post/(?P<user_pk>\d+)/$', PostDetail.as_view(), name='post-detail'),
]