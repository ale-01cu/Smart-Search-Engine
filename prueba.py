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

# # Preprocesamiento de documentos
# stop_words = set(stopwords.words('spanish'))
# stemmer = PorterStemmer()

# # Función para preprocesar documentos
# def preprocess(doc):
#     tokens = word_tokenize(doc.lower())
#     tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
#     tokens = [stemmer.stem(token) for token in tokens]
#     return Counter(tokens)

# # Convertimos los documentos a vectores de términos
# term_vectors = [preprocess(doc) for doc in documents]

# # Función para calcular la similitud de coseno entre dos vectores
# def cosine_similarity(vec1, vec2):
#     intersection = set(vec1.keys()) & set(vec2.keys())
#     numerator = sum([vec1[x] * vec2[x] for x in intersection])
#     sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
#     sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
#     denominator = math.sqrt(sum1) * math.sqrt(sum2)
#     if not denominator:
#         return 0.0
#     else:
#         return float(numerator) / denominator

# # Función para buscar documentos que contengan términos específicos
# def search(query):
#     query_vector = preprocess(query)
#     scores = [(i, cosine_similarity(query_vector, term_vectors[i])) for i in range(len(term_vectors))]
#     print(scores)
#     scores = sorted(scores, key=lambda x: x[1], reverse=True)
#     return [documents[i] for (i, score) in scores if score > 0]

# # Ejemplo de búsqueda
# query = "viva"
# results = search(query)
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
import gensim

# Cargar el modelo en un objeto KeyedVectors
model = gensim.models.KeyedVectors.load_word2vec_format('cc.es.300.vec', binary=False)

# Obtener el vector para una palabra específica
vector = model['palabra']

# Calcular la similitud entre dos palabras
similarity = model.similarity('palabra1', 'palabra2')

# Obtener las palabras más similares a una palabra dada
similar_words = model.most_similar('palabra')

# import requests

# response = requests.get('http://img.omdbapi.com/?apikey=[4548872e-ed65-4610-9412-b0ec45a8e2c6]&')
# print(response.json())