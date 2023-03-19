from rest_framework import viewsets, status, generics, filters
from App_Buscador.models import Contenido
from .serializers import SerializerContenido
from rest_framework.response import Response
from App_Buscador.helpers.ordenamiento_Quicksort import Quicksort, burbuja
from App_Buscador.helpers.procesar_texto import search
import time

# Create your views here.
# 
# 
class ContenidoView(viewsets.ModelViewSet):
    queryset = Contenido.objects.all()
    serializer_class = SerializerContenido

# import operator
# from functools import reduce
# from django.db.models import Q, Sum, Case, When, IntegerField
# class BusquedaView(viewsets.ViewSet):
#   def list(self, request, busqueda):
#     query_busqueda = request.query_params.get('busqueda', '').lower()
#     palabras_claves = query_busqueda.split(" ")
    
#     if not palabras_claves:
#         # Si no hay palabras clave, devolver todos los contenidos
#         queryset = Contenido.objects.all()
#     else:
#         # Si hay palabras clave, filtrar los contenidos que las contengan
#         queryset = Contenido.objects.filter(
#             reduce(operator.and_, (Q(categoria__icontains=palabra) | 
#                                     Q(titulo__icontains=palabra) | 
#                                     Q(descripcion__icontains=palabra) | 
#                                     Q(fecha_de_estreno__icontains=palabra) | 
#                                     Q(generos__icontains=palabra) 
#                                     for palabra in palabras_claves))
#         )
        
#     # Ordenar los resultados por cantidad de coincidencias
#     queryset = queryset.annotate(coincidencias=Sum(
#         Case(
#             When(
#                 reduce(operator.and_, (Q(categoria__icontains=palabra) | 
#                                         Q(titulo__icontains=palabra) | 
#                                         Q(descripcion__icontains=palabra) | 
#                                         Q(fecha_de_estreno__icontains=palabra) | 
#                                         Q(generos__icontains=palabra) 
#                                         for palabra in palabras_claves)), 
#                 then=1), 
#             output_field=IntegerField()
#         )
#     )).order_by('-coincidencias')
    
#     # Serializar los resultados y devolverlos
#     serializer = SerializerContenido(queryset, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
    

class BusquedaView(viewsets.ViewSet):
  def list(self, request, busqueda):
  
    start_time = time.time()
    query_busqueda = request.query_params.get('busqueda', None).lower()

    querySets = Contenido.objects.all()
    serializer = SerializerContenido(querySets, many=True)

    resultado = []
          
    # Imprimir contenido del serializer en formato JSON
    for i in serializer.data:
      todo = f"{i['categoria']}s {i['titulo']} {i['descripcion']} {i['fecha_de_estreno']} {i['generos']}".lower()
      coincidencias = search(query_busqueda, todo)
      if coincidencias > 0: resultado.append({"e": i, "c":coincidencias})
      
    ordenados = sorted(resultado, key=lambda x: x['c'], reverse=True)
    respuesta = [e['e'] for e in ordenados]
    
    end_time = time.time()
    tiempo_total = round(end_time - start_time, 4)
    print(f"La busqueda tardo {tiempo_total} segundos en ejecutarse")
    
    return Response(respuesta, status=status.HTTP_200_OK)
