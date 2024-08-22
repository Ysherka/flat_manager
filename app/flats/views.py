from django.views.generic import DetailView, ListView

from .models import Flat

class AllFlatsView(ListView):
    model = Flat
    template_name = 'flats/flats.html'
    context_object_name = 'flats'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# class FlatView(DetailView):
#     model = Flat
#     template_name = 'flats/detail_flat.html'
#     context_object_name = 'flat'
#
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context