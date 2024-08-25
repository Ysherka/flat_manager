from django.urls import path

from .views import *

app_name = 'flats'

urlpatterns = [
    path('', AllFlatsView.as_view(), name='all_flats'),
    path('<int:flat_id>', FlatView.as_view(), name='flat'),
]