from django.conf.urls import url, include

from utils.sms.apis import SendSMS

urlpatterns = [
    url(r'^post/', include('post.urls.apis', namespace='post')),
    url(r'^member/', include('member.urls.apis',  namespace='member')),
    url(r'^sms/$', SendSMS.as_view(), name='sms')
    ]

