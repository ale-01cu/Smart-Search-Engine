from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import views
from rest_framework.views import Response
from rest_framework.request import Request
from apps.pubs.models import PubsModel
from rest_framework import status


class ListPubs(views.APIView):
    def get(self, request: Request):
        page = int(request.query_params.get('page'))
        pubs = PubsModel().list_all(page=page)
        
        data = {
            "previous": page-1 if page>0 else 0,
            "next": page+1,
            "pubs": pubs
        }
        
        return Response(
            data=data, 
            status=status.HTTP_200_OK
        )
