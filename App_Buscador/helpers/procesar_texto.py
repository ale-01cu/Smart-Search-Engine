import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from collections import Counter

def procesar(texto):
  
  stop_words = set(stopwords.words('spanish'))

  # Tokenizar la frase
  tokens = word_tokenize(texto)
  stemmer = SnowballStemmer('spanish')

  # Eliminar las palabras vacías
  tokens_limpios =  [ stemmer.stem(token.lower()) for token in tokens if token.isalpha() and token not in stop_words ]
  palabras_Claves_sin_repetirse = list(Counter(tokens_limpios).keys())
  
  return palabras_Claves_sin_repetirse


def search(query, document):
  document_procesado = procesar(document)
  doc_text = " ".join(document_procesado)
  
  coincidencias = 0

  for querys in query:
    if doc_text.count(querys) > 0: coincidencias += 1
  
  mensaje = f'Comparacion:\n query: {query} \n doc: {document_procesado} \n coincidencias {coincidencias}'
  print(mensaje)
  
  return coincidencias

