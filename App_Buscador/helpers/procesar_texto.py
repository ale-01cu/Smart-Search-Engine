import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('wordnet')


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter

def procesar(**keyargs):
  texto = keyargs['texto']
  
  stop_words = set(stopwords.words('spanish'))

  # Tokenizar la frase
  words = word_tokenize(texto)
  stemmer = PorterStemmer()

  # Eliminar las palabras vacías
  filtered_words = [token for token in words if token.isalpha() and token not in stop_words]
  stemmed_words = [stemmer.stem(word) for word in filtered_words]
  palabras_Claves_sin_repetirse = list(Counter(stemmed_words).keys())
  
  return palabras_Claves_sin_repetirse


def search(query, document):
  query_procesada = procesar(texto=query)
  document_procesado = procesar(texto=document)
  doc_text = " ".join(document_procesado)
  
  coincidencias = 0
  similitud = 0

  for querys in query_procesada:
    coincidencias += doc_text.count(querys)
  
  
  mensaje = f'Comparacion:\n query: {query_procesada} \n doc: {document_procesado}'
  print(mensaje)
  
  return coincidencias

