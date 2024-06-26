from pubs.views import ListPubs
from django.urls import path

url_pattern = [
    path('pubs/', ListPubs.as_view())
]
