from django.views.generic import DetailView, ListView

from .models import Flat

import json

class AllFlatsView(ListView):
    model = Flat
    template_name = 'flats/flats.html'
    context_object_name = 'flats'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coords'] = json.dumps(
            [
                {
                    'url': flat.get_url(),
                    'long': flat.longitude,
                    'lat': flat.latitude,
                    'price': flat.price
                }
                for flat in context['flats']
            ]
        )
        print(context['coords'])
        return context


class FlatView(DetailView):
    model = Flat
    template_name = 'flats/detail_flat.html'
    pk_url_kwarg = 'flat_id'
    context_object_name = 'flat'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context