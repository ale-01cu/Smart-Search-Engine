from apps.pubs.views import ListPubs
from django.urls import path

urlpatterns = [
    path('pubs/', ListPubs.as_view())
]
