import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('wordnet')


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def procesar(**keyargs):
  texto = keyargs['texto']
  
  stop_words = set(stopwords.words('spanish'))

  # Tokenizar la frase
  words = word_tokenize(texto)
  stemmer = PorterStemmer()

  # Eliminar las palabras vacías
  filtered_words = [word for word in words if word.casefold() not in stop_words]
  stemmed_words = [stemmer.stem(word) for word in filtered_words]
  
  mensaje = f'Comparacion:\n original: {texto} \n modificado: {stemmed_words}'
  print(mensaje)

  return stemmed_words

