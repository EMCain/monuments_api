from django.conf.urls import url

from .views import MonumentView

urlpatterns = [
    url(r'^(?P<monument_id>[0-9]+)/$', MonumentView.as_view(), name='Single Monument'),
]