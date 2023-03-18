import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('wordnet')


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stop_words = set(stopwords.words('spanish'))

text = "peliculas que son de accion"

# Tokenizar la frase
words = word_tokenize(text)
stemmer = PorterStemmer()

# Eliminar las palabras vacías
filtered_words = [word for word in words if word.casefold() not in stop_words]

stemmed_words = [stemmer.stem(word) for word in filtered_words]

print(stemmed_words)