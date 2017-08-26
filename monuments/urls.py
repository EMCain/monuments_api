from django.conf.urls import url

from .views import MonumentView

urlpatterns = [
    url(r'^<monument_id>', MonumentView.as_view(), 'Single Monument'),
]