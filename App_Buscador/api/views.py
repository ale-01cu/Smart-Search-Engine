from django.shortcuts import render
from rest_framework import viewsets, status
from App_Buscador.models import Contenido
from .serializers import SerializerContenido
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from App_Buscador.helpers.ordenamiento_Quicksort import Quicksort, burbuja
from App_Buscador.helpers.procesar_texto import procesar
import spacy
from rank_bm25 import BM25Okapi
from tqdm import tqdm

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

from txtai.embeddings import Embeddings

# class BusquedaView(viewsets.ViewSet):
#     def list(self, request, busqueda):
#         nlp = spacy.load("es_core_news_md")

#         entrada = "pelicula donde se maten a muchas personas y hayan carros voladores que hablen entre ellos y conspiren en contra de una revolucion diabolica del 1980"
#         doc = nlp(entrada)
            
#         # Saca palabras que no interesan
#         palabras_no_vacias = [token.text for token in doc if not token.is_stop]
        
#         # forma base 
#         document = nlp(" ".join(palabras_no_vacias))
#         forma_base = [token.lemma_ for token in document]
#         print(forma_base)



#         return Response({"a": "hola buenos dias"})


# class BusquedaView(viewsets.ViewSet):
#   def list(self, request, busqueda):
#     query_busqueda = request.query_params.get('busqueda', '').lower()
#     palabras_claves = query_busqueda.split()
    
#     if not palabras_claves:
#         # Si no hay palabras clave, devolver todos los contenidos
#         queryset = Contenido.objects.all()
#     else:
#         # Si hay palabras clave, filtrar los contenidos que las contengan
#         queryset = Contenido.objects.filter(
#             reduce(operator.and_, (Q(categoria__icontains=palabra) | 
#                                     Q(titulo__icontains=palabra) | 
#                                     Q(descripcion__icontains=palabra) | 
#                                     Q(fecha__icontains=palabra) | 
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
#                                         Q(fecha__icontains=palabra) | 
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
  
    query_busqueda = request.query_params.get('busqueda', None).lower()
    palabras_claves = procesar(texto=query_busqueda)
    
    querySets = Contenido.objects.all()
    serializer = SerializerContenido(querySets, many=True)

    resultado = []
    valor_max = 0
    promedio = 0
      
    # Imprimir contenido del serializer en formato JSON
    for i in serializer.data:
      id, categoria, titulo, descripcion, fecha, generos = i.values()
      todo = f"{categoria}s {titulo} {descripcion} {fecha} {generos}".lower()
      todo_procesado = procesar(texto=todo)
      
      print("relacion")
      print(palabras_claves)
      print(todo_procesado)
      
      for j in palabras_claves:
        if j in todo_procesado:
          promedio += 1
        
      if valor_max < promedio: valor_max = promedio
      if promedio > 0 and promedio >= len(palabras_claves):
        resultado.append({'e': i, 'coincidencias': promedio})
      promedio = 0

    respuesta = list(map(lambda x: x['e'], resultado))

    return Response(respuesta, status=status.HTTP_200_OK)
