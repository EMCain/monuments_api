from json import dumps

from django.views.generic import DetailView, ListView

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

    def dispatch(self, request, *args, **kwargs):
        if not self.pk_url_kwarg:
            self.pk_url_kwarg = kwargs['monument_id']
        return super(MonumentView, self).dispatch(self, request, pk_url_kwarg=self.pk_url_kwarg, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        self.mock_json['id'] = self.pk_url_kwarg or None
        return dumps(self.mock_json)

class MonumentsNearMe(ListView):
    pass