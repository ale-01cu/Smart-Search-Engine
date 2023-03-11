from django.shortcuts import render
from rest_framework import viewsets
from App_Buscador.models import Contenido
from .serializers import SerializerContenido
from rest_framework.response import Response

# Create your views here.
class ContenidoView(viewsets.ViewSet):
  
  def list(self, request):
    querySets = Contenido.objects.all()
    serializer = SerializerContenido(querySets, many=True)
    return Response(serializer.data)
