from django.shortcuts import render
from rest_framework import viewsets, status
from App_Buscador.models import Contenido
from .serializers import SerializerContenido
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import json

# Create your views here.
class ContenidoView(viewsets.ViewSet):
  def list(self, request):
    querySets = Contenido.objects.all()
    serializer = SerializerContenido(querySets, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None):
    try:
      querySet = Contenido.objects.get(id=pk)
      data = SerializerContenido(querySet)
      return Response(data.data)
    except:
      return Response({'msg':'Ha ocurrido un error al buscar ese id en la DB'}, status=status.HTTP_404_NOT_FOUND)


class BusquedaView(viewsets.ViewSet):
  def list(self, request):
    query_busqueda = request.query_params.get('busqueda', None)
    querySets = Contenido.objects.all()
    serializer = SerializerContenido(querySets, many=True)
    
    print(query_busqueda)
    
    # Imprimir contenido del serializer en formato JSON
    for i in serializer.data:
      id, categoria, titulo, descripcion, fecha, generos = i.values()
      todo = f"{categoria} {titulo} {descripcion} {fecha} {generos}"
      print(todo)
      
    
    return Response(serializer.data)
    
