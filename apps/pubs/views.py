from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import views
from rest_framework.views import Response
from rest_framework.request import Request


class ListPubs(views.APIView):
    def get(self, request: Request):
        pass
