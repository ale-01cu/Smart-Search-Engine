from rest_framework import viewsets, status, generics, filters
from App_Buscador.models import Contenido
from .serializers import SerializerContenido
from rest_framework.response import Response
from App_Buscador.helpers.ordenamiento_Quicksort import Quicksort, burbuja
from App_Buscador.helpers.procesar_texto import search, procesar
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
  
    # Se obtiene el tiempo en el que se inicia la ejecución de la búsqueda
    start_time = time.time()

    # Se obtiene el parámetro "busqueda" de la URL y se convierte a minúsculas
    query_busqueda = request.query_params.get('busqueda', None).lower()
    query_procesada = procesar(query_busqueda)

    # Se obtienen todos los objetos Contenido de la base de datos
    querySets = Contenido.objects.all()

    # Se serializan los objetos obtenidos para poder manipularlos en Python
    serializer = SerializerContenido(querySets, many=True)

    resultado = []
          
    # Se itera sobre los objetos serializados para buscar coincidencias con la búsqueda
    for i in serializer.data:
      # Se concatenan todos los campos de un objeto en un string y se convierte a minúsculas
      todo = f"{i['categoria']}s {i['titulo']} {i['descripcion']} {i['fecha_de_estreno']} {i['generos']}".lower()
      # Se llama a la función search para buscar coincidencias entre la búsqueda y el string concatenado
      coincidencias = search(query_procesada, todo)
      # Si se encontraron coincidencias, se agrega el objeto y el número de coincidencias a la lista de resultados
      if coincidencias > 0: resultado.append({"e": i, "c":coincidencias})
      
    # Se ordenan los resultados por número de coincidencias, de mayor a menor
    ordenados = sorted(resultado, key=lambda x: x['c'], reverse=True)
    # Se crea una lista solo con los objetos ordenados (sin el número de coincidencias)
    respuesta = [e['e'] for e in ordenados]
    
    # Se obtiene el tiempo en el que se termina la ejecución de la búsqueda
    end_time = time.time()
    # Se calcula el tiempo total de ejecución
    tiempo_total = round(end_time - start_time, 4)
    # Se imprime el tiempo total de ejecución
    print(f"La busqueda tardo {tiempo_total} segundos en ejecutarse")
    
    # Se devuelve la lista de objetos ordenados como respuesta
    return Response(respuesta, status=status.HTTP_200_OK)