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
        query = request.query_params.get('page')
        try:
            query = int(query)

        except:
            query = 1
            
        page = query if query and int(query) > 0 else 1
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
    

class GetPubById(views.APIView):
    def get(self, request: Request, pub_id: int):
        pub = PubsModel().get_by_id(pub_id)
        return Response(pub, status=status.HTTP_200_OK)

