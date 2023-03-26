# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from nltk.stem import PorterStemmer
# from collections import Counter
# import math

# # Definimos una lista de documentos de ejemplo
# documents = [
#     "Este es un documento creado por mi donde lo uso de ejemplo para un motor de busqueda documento",
#     "Almejas voladoras es lo ultimo en tecnologia de la nasa",
#     "Viva el comunismo democratico capitalista"
# ]

# # Descargamos las stopwords y definimos un stemmer
# stop_words = set(stopwords.words('spanish'))
# stemmer = PorterStemmer()

# # Función para preprocesar documentos
# def preprocess(doc):
#     # Convertimos el texto a minúsculas y tokenizamos las palabras
#     tokens = word_tokenize(doc.lower())
#     # Eliminamos los signos de puntuación y las stopwords
#     tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
#     # Aplicamos stemming a cada palabra
#     tokens = [stemmer.stem(token) for token in tokens]
#     # Devolvemos un diccionario con el recuento de cada palabra
#     return Counter(tokens)

# # Convertimos los documentos a vectores de términos
# term_vectors = [preprocess(doc) for doc in documents]

# # Función para calcular la similitud de coseno entre dos vectores
# def cosine_similarity(vec1, vec2):
#     print("el vector 1", vec1)
#     print("el vector 2", vec2)
#     # Calculamos la intersección de las claves de los dos vectores
#     intersection = set(vec1.keys()) & set(vec2.keys())
#     print("intersectiiononnnnn",intersection)
#     # Calculamos el numerador del coeficiente de similitud de coseno
#     numerator = sum([vec1[x] * vec2[x] for x in intersection])
#     print("numerator ", numerator)
#     # Calculamos la norma euclidiana de cada vector
#     sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
#     sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
#     # Calculamos el denominador del coeficiente de similitud de coseno
#     denominator = math.sqrt(sum1) * math.sqrt(sum2)
#     # Manejamos la división por cero
#     if not denominator:
#         return 0.0
#     else:
#         return float(numerator) / denominator

# # Función para buscar documentos que contengan términos específicos
# def search(query):
#     # Convertimos la consulta en un vector de términos
#     query_vector = preprocess(query)
#     # Calculamos el coeficiente de similitud de coseno entre la consulta y cada documento
#     scores = [(i, cosine_similarity(query_vector, term_vectors[i])) for i in range(len(term_vectors))]
#     # Imprimimos los resultados de similitud
#     print(scores)
#     # Ordenamos los documentos por similitud descendente y devolvemos los que tengan una similitud positiva
#     scores = sorted(scores, key=lambda x: x[1], reverse=True)
#     return [documents[i] for (i, score) in scores if score > 0]

# # Ejemplo de búsqueda
# query = "doc"
# results = search(query)
# # Imprimimos los resultados de la búsqueda
# print(f"Resultados de búsqueda para '{query}':")
# print(results)


# from simhash import Simhash

# # Definir las palabras a comparar como cadenas de caracteres
# word1 = 'serie de dragones'
# word2 = 'seri casa dragon tremenda mierda aventura fantasia'

# # Crear listas de tuplas con las características de cada palabra
# features1 = [(c, word1.count(c)) for c in set(word1)]
# features2 = [(c, word2.count(c)) for c in set(word2)]

# # Obtener los Simhash de cada palabra
# hash1 = Simhash(features1)
# hash2 = Simhash(features2)

# # Calcular la distancia entre los Simhash
# distance = hash1.distance(hash2)

# # Calcular la similitud
# similarity = 1.0 - (float(distance) / len(word1))

# # Imprimir el resultado
# print(f"La similitud entre {word1} y {word2} es: {similarity}")

#### Para mejor

#gensim ---3 Word2Vec 
# import gensim

# # Cargar el modelo en un objeto KeyedVectors
# model = gensim.models.KeyedVectors.load_word2vec_format('cc.es.300.vec', binary=False)

# # Obtener el vector para una palabra específica
# vector = model['palabra']

# # Calcular la similitud entre dos palabras
# similarity = model.similarity('palabra1', 'palabra2')

# # Obtener las palabras más similares a una palabra dada
# similar_words = model.most_similar('palabra')

# import requests

# response = requests.get('http://img.omdbapi.com/?apikey=[4548872e-ed65-4610-9412-b0ec45a8e2c6]&')
# print(response.json())






# todo mas optimizado con pandas y numpy 
# import time
# import numpy as np
# import pandas as pd
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from nltk.stem import PorterStemmer
# from collections import Counter
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class ContenidoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contenido
#         fields = '__all__'

# class ContenidoList(APIView):
#     def get(self, request):
#         busqueda = request.query_params.get('busqueda', None)
#         if busqueda:
#             start_time = time.time()

#             # Cargar los datos en un DataFrame
#             df = pd.DataFrame(list(Contenido.objects.all().values()))

#             # Convertir todos los campos de texto a minúsculas
#             df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)

#             # Concatenar todos los campos de texto en un solo campo
#             df['todo'] = df[['categoria', 'titulo', 'descripcion', 'fecha_de_estreno', 'generos']].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)

#             # Tokenizar y procesar la consulta
#             query = procesar(busqueda)
#             query_array = np.array(query)

#             # Tokenizar y procesar cada campo de texto en el DataFrame
#             documents = df['todo'].apply(lambda x: procesar(x))
#             documents_array = np.array(documents.tolist())

#             # Vectorizar el procesamiento de texto y las comparaciones de cadenas utilizando NumPy
#             counts = np.array([np.isin(query_array, doc).sum() for doc in documents_array])

#             # Ordenar los resultados por número de coincidencias
#             df['coincidencias'] = counts
#             df = df.sort_values('coincidencias', ascending=False)

#             # Eliminar el campo 'todo' y devolver los resultados
#             df = df.drop('todo', axis=1)
#             resultados = df.to_dict(orient='records')

#             end_time = time.time()
#             tiempo_total = round(end_time - start_time, 4)
#             print(f"La búsqueda tardó {tiempo_total} segundos en ejecutarse")

#             return Response(resultados, status=status.HTTP_200_OK)

#         else:
#             # Si no se proporciona un parámetro de búsqueda, devolver todos los objetos Contenido
#             querySets = Contenido.objects.all()
#             serializer = ContenidoSerializer(querySets, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)


# def procesar(texto):
#     stop_words = set(stopwords.words('spanish'))

#     # Tokenizar la frase
#     words = word_tokenize(texto)
#     stemmer = PorterStemmer()

#     # Eliminar las palabras vacías
#     filtered_words = [token for token in words if token.isalpha() and token not in stop_words]
#     stemmed_words = [stemmer.stem(word) for word in filtered_words]
#     palabras_Claves_sin_repetirse = list(Counter(stemmed_words).keys())

#     return palabras_Claves
from nltk.corpus import stopwords # importa el conjunto de palabras vacías de NLTK
from nltk.tokenize import word_tokenize # importa el tokenizador de palabras de NLTK
from nltk.stem import SnowballStemmer # importa el stemmer de nieve de NLTK
from collections import Counter # importa la clase Counter para contar elementos
from nltk import NaiveBayesClassifier, classify # importa el clasificador Naive Bayes de NLTK y la función classify
import math # importa el módulo de matemáticas de Python
from operator import itemgetter # importa la función itemgetter del módulo operator

# crea una instancia de SnowballStemmer para español
stemmer = SnowballStemmer('spanish')

# obtiene el conjunto de palabras vacías de español de NLTK
stop_words = set(stopwords.words('spanish'))

# lista de documentos de ejemplo
docs = [
  "Documento de prueba para saber la fiabilidad de machine learning",
  "Documento relacionado con peliculas de todo tipo en cualquier contexto",
  "Esto no es un documento sino un manifiesto hacerca de series de todo tipo",
  "Esto es un documento de prueba para un motor de busqueda utilizando machine learning"
]

# función para procesar un texto
def process(entrada):
    # tokeniza la entrada
    tokens = word_tokenize(entrada)
    # aplica el stemmer a cada token y lo agrega a una lista si cumple con ciertos criterios
    tokens_limpios = [stemmer.stem(token.lower()) for token in tokens if token.isalpha() and token not in stop_words]
    # cuenta la cantidad de veces que aparece cada token y los devuelve en un diccionario
    counter = Counter(tokens_limpios)
    return dict(counter)
  
# función para calcular los IDFs de los términos
def calculate_idfs(vocabulary, doc_features):
  # crea un diccionario vacío para almacenar los IDFs
  doc_idfs = {}
  # itera por cada término del vocabulario
  for term in vocabulary:
    doc_count = 0
    # itera por cada documento en el conjunto de documentos
    for doc_id in doc_features.keys():
      # obtiene los términos del documento actual
      terms = doc_features.get(doc_id)
      # si el término actual aparece en el documento actual, aumenta el contador
      if term in terms.keys():
        doc_count += 1
    # calcula el IDF del término actual y lo almacena en el diccionario de IDFs
    doc_idfs[term] = math.log(
      float(len(doc_features.keys()))/
      float(1 + doc_count), 10)
  # devuelve el diccionario de IDFs
  return doc_idfs

def vectorize_idf(input_terms, input_idfs, vocabulary):
  # Crea un diccionario vacío para almacenar los vectores de salida
  output = {}
  
  # Itera sobre los términos de entrada para cada documento
  for item_id in input_terms.keys():
    terms = input_terms.get(item_id)
    output_vector = []
    
    # Itera sobre todo el vocabulario
    for term in vocabulary:
      # Si el término actual está presente en el documento actual, calcula su puntuación IDF y multiplica por la frecuencia del término en el documento
      if term in terms.keys():
        output_vector.append(input_idfs.get(term)*float(terms.get(term)))
      # Si el término actual no está presente en el documento actual, su puntuación IDF es 0 y su frecuencia es 0
      else:
        output_vector.append(float(0))
    
    # Añade el vector de salida para el documento actual al diccionario de salida
    output[item_id] = output_vector
    
  # Devuelve el diccionario de vectores de salida
  return output


def length(vector):
  # Calcula la longitud del vector utilizando la fórmula euclidiana
  sq_length = 0
  for index in range(0, len(vector)):
    sq_length += math.pow(vector[index], 2)
  return math.sqrt(sq_length)


def dot_product(vector1, vector2):
  # Calcula el producto punto de dos vectores, solo si tienen la misma longitud
  if len(vector1) == len(vector2):
    dot_prod = 0
    for index in range(0, len(vector1)):
      # Ignora los valores de 0 en ambos vectores, ya que no contribuyen al producto punto
      if not vector1[index] == 0 and not vector2[index] == 0:
        dot_prod += vector1[index] * vector2[index]
    return dot_prod
  else:
    # Si los vectores no tienen la misma longitud, devuelve una cadena de texto indicando que la dimensionalidad no coincide
    return "Unmatching dimensionality"


def calculate_cosine(query, document):
  # Calcula el coseno del ángulo entre dos vectores utilizando la fórmula de coseno
  media = length(query) * length(document)
  if media == 0:
    return 0
  else:
    cosine = dot_product(query, document) / media
    return cosine

# doc_vectors = vectorize_idf(doc_terms, doc_idfs, all_terms)

# Pedimos al usuario que escriba algo y procesamos su entrada
entrada = input("Escriba algo: ")
entrada_procesada = process(entrada)

# Procesamos los documentos
docs_procesados = [ process(doc) for i, doc in enumerate(docs) ]

# Creamos un diccionario con los documentos procesados
dict_docs = {}
for i, doc in enumerate(docs_procesados):
  dict_docs[f"doc{i}"] = doc

# Calculamos los idfs de los términos en la entrada y en los documentos
doc_idfs = calculate_idfs(entrada_procesada, dict_docs)

# Vectorizamos los documentos con sus idfs
doc_vectors = vectorize_idf(dict_docs, doc_idfs, entrada_procesada)

# Obtenemos el vector de la entrada
query_vector = list(doc_idfs.values())

# Calculamos los cosenos entre el vector de la entrada y los vectores de los documentos
query_cosines = {}
for doc_id, doc_vector in doc_vectors.items():
    cosine = calculate_cosine(query_vector, doc_vector)
    query_cosines[doc_id] = cosine

# Ordenamos los documentos según su relevancia y los imprimimos
for doc_id, cosine in sorted(query_cosines.items(), key=itemgetter(1), reverse=True):
    print(f"Documento: {doc_id} - Relevancia: {cosine}")