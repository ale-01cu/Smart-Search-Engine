from rest_framework import viewsets, status, generics, filters
from App_Buscador.models import Contenido
from .serializers import SerializerContenido
from rest_framework.response import Response
from App_Buscador.helpers.procesar_texto import search, procesar
from App_Buscador.helpers.clase_resultados_query import Resultados, diccionario_resultados
from .pagination import ContenidoPagination
import time

# Create your views here.
# 
# 
class ContenidoView(viewsets.ModelViewSet):
    queryset = Contenido.objects.all()
    serializer_class = SerializerContenido
    pagination_class = ContenidoPagination
    
    def retrieve(self, request, *args, **kwargs):
      q = self.request.query_params.get('q', None)
      id_elemnto = kwargs.get('pk')
      
      if q:
        query_procesada = procesar(q)
        query_procesada_texto = " ".join(query_procesada)
        object_resultados = diccionario_resultados[query_procesada_texto]
        object_resultados.actualizarInteraccion(id_elemnto)
        
      return super().retrieve(request, *args, **kwargs)

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

from elasticsearch_dsl import Search
from elasticsearch_dsl import Q

class BusquedaView(viewsets.ViewSet):
   
  def list(self, request, busqueda):
      query_busqueda = request.query_params.get('busqueda', None).lower()
      procesada = ' '.join(procesar(query_busqueda))
      q = Q('bool',
          should=[
              Q('multi_match', query=procesada, fields=['titulo', 'categoria', 'generos', 'descripcion']),
              Q('more_like_this', like=procesada, fields=['titulo', 'categoria', 'generos', 'descripcion']),
          ],
          minimum_should_match=1,
      )

      # Agregar la búsqueda wildcard para tener en cuenta las palabras que contienen la consulta
      for palabra in procesada.split():
          q |= Q('wildcard', titulo={'value': f'*{palabra}*'}) | Q('wildcard', categoria={'value': f'*{palabra}*'}) | Q('wildcard', generos={'value': f'*{palabra}*'}) | Q('wildcard', descripcio={'value': f'*{palabra}*'})

      s = Search(index='contenido').query(q)
      response = s.execute()

      resultados = []
      for hit in response.hits:
          resultados.append(hit.to_dict())

      return Response(resultados, status=status.HTTP_200_OK)


    # resultados_por_querys = {}
  
    # # Se obtiene el tiempo en el que se inicia la ejecución de la búsqueda
    # start_time = time.time()

    # # Se obtiene el parámetro "busqueda" de la URL y se convierte a minúsculas
    # query_busqueda = request.query_params.get('busqueda', None).lower()
    # query_procesada = procesar(query_busqueda)
    # query_procesada_texto = " ".join(query_procesada)
    
    # if " ".join(query_procesada) in diccionario_resultados.keys():
    #   return Response(diccionario_resultados[query_procesada_texto].resultados, status=status.HTTP_200_OK)

    # querySets = Contenido.objects.all()
    # serializer = SerializerContenido(querySets, many=True)

    # resultado = []
          
    # # Se itera sobre los objetos serializados para buscar coincidencias con la búsqueda
    # for i in serializer.data:
    #   todo = f"{i['categoria']}s {i['titulo']} {i['descripcion']} {i['fecha_de_estreno']} {i['generos']}".lower()
    #   coincidencias = search(query_busqueda, todo)
    #   if coincidencias > 0: resultado.append({"e": i, "c":coincidencias})
      
    # # Se ordenan los resultados por número de coincidencias, de mayor a menor
    # ordenados = sorted(resultado, key=lambda x: x['c'], reverse=True)
    # # Se crea una lista solo con los objetos ordenados (sin el número de coincidencias)
    # respuesta = [e['e'] for e in ordenados]
    
    # nuevo_resultado = Resultados(query_procesada, respuesta)
    # nuevo_resultado.entrenar()
    # respuesta = nuevo_resultado.resultados.copy()
    
    # diccionario_resultados[" ".join(query_procesada)] = nuevo_resultado
  
    # # Se obtiene el tiempo en el que se termina la ejecución de la búsqueda
    # end_time = time.time()
    # # Se calcula el tiempo total de ejecución
    # tiempo_total = round(end_time - start_time, 2)
    # respuesta.append(tiempo_total)
    # # Se imprime el tiempo total de ejecución
    # print(f"La busqueda tardo {tiempo_total} segundos en ejecutarse")
    
    # # Se devuelve la lista de objetos ordenados como respuesta
    # return Response(respuesta, status=status.HTTP_200_OK)