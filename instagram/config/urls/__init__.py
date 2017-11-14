from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from . import apis, views

urlpatterns = [
    url(r'^', include(views)),
    url(r'^api/', include(apis, namespace='api')),
]

urlpatterns += static(
    settings.base.MEDIA_URL,
    document_root=settings.base.MEDIA_ROOT,
)
