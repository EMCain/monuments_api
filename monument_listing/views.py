# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.generic import DetailView, ListView, View

from json import dumps
# see https://ccbv.co.uk/ for reference

class MonumentView(DetailView):
    mock_json = {
        'id': None,
        'title': 'My Favorite Monument',
        'summary': 'This will be some text telling you about the monument.',
        'header_img': 'https://en.wikipedia.org/wiki/Monument#/media/File:Harvest_Moon_rises_over_Washington.jpg',
        'coordinates': {
            'lng': 0,
            'lat': 0,
        },
        'info': {}
    }
    pk_url_kwarg = 'monument_id'

    def get_object(self, queryset=None):
        # TODO: look up the Monument
        return None

    def get(self, request, *args, **kwargs):
        self.mock_json['id'] = self.kwargs.get(self.pk_url_kwarg, None)
        json_content = dumps(self.mock_json)
        return HttpResponse(json_content)

class MonumentsNearMe(ListView):
    pass