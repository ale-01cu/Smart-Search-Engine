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
      print(pk)
      print("entre a detalle")
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
    
    palabras_claves = query_busqueda.split(" ")
    resultado = []
    valor_max = 0
    palabras_y_coincidencias = []
    promedio = 0
      
    # Imprimir contenido del serializer en formato JSON
    for i in serializer.data:
      id, categoria, titulo, descripcion, fecha, generos = i.values()
      todo = f"{categoria} {titulo} {descripcion} {fecha} {generos}"
      
      
      for j in palabras_claves:
        repeticiones = todo.count(j)
        palabras_y_coincidencias.append({j: repeticiones})
        promedio += repeticiones
        
      
      if valor_max < promedio: valor_max = promedio
      resultado.append({'e': i, 'datos': {'coincidencias': palabras_y_coincidencias, 'total': promedio}})
      palabras_y_coincidencias = []
      promedio = 0
    
    print(resultado)
    respuesta = []
    for k in resultado: 
      if valor_max != 0 and k['datos']['total'] == valor_max:
        respuesta.append(k['e'])
      
    
    return Response(respuesta)
    
