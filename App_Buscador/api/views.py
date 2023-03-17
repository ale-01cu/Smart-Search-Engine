from django.shortcuts import render
from rest_framework import viewsets, status
from App_Buscador.models import Contenido
from .serializers import SerializerContenido
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from App_Buscador.helpers.ordenamiento_Quicksort import Quicksort, burbuja
from App_Buscador.helpers.palabras_para_excluir import palabras

# Create your views here.
# 
# 
class ContenidoView(viewsets.ModelViewSet):
    queryset = Contenido.objects.all()
    serializer_class = SerializerContenido
# 
# class ContenidoView(viewsets.ViewSet):
#   def list(self, request):
#     print("todo el contenido")
#     querySets = Contenido.objects.all()
#     serializer = SerializerContenido(querySets, many=True)
#     return Response(serializer.data)
  
#   def retrieve(self, request, pk=None):
#     try:
#       print(pk)
#       print("entre a detalle")
#       querySet = Contenido.objects.get(id=pk)
#       data = SerializerContenido(querySet)
#       return Response(data.data)
#     except:
#       return Response({'msg':'Ha ocurrido un error al buscar ese id en la DB'}, status=status.HTTP_404_NOT_FOUND)

#   def create(self)


class BusquedaView(viewsets.ViewSet):
  def list(self, request, busqueda):
    print("en la busqueda")
    print(busqueda)
    
    query_busqueda = request.query_params.get('busqueda', None).lower()
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
      todo = f"{categoria}s {titulo} {descripcion} {fecha} {generos}".lower()
      
      
      for j in palabras_claves:
        if not (j in palabras):
          repeticiones = todo.count(j)
          promedio += repeticiones
          palabras_y_coincidencias.append({j: repeticiones})

        else:
          print(f"la palabra '{j}' esta en la lista de palabras para excliuir...")
          
      
      if valor_max < promedio: valor_max = promedio
      if promedio > 0:
        resultado.append({'e': i, 'datos': {'coincidencias': palabras_y_coincidencias, 'total': promedio}})
      palabras_y_coincidencias = []
      promedio = 0

    burbuja(resultado)
    respuesta = list(map(lambda x: x['e'], resultado))

    return Response(respuesta, status=status.HTTP_200_OK)
    
