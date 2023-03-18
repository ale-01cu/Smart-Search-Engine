import spacy

nlp = spacy.load("es_core_news_md")

def procesar(**keyargs):
    doc = nlp(keyargs['texto'])
    lemma = [token.lemma_ for token in doc]
    print(lemma)
    
    palabras_no_vacias = [token.text for token in nlp(" ".join(lemma)) if not token.is_stop]
    palabras_con_peso = [token.text for token in nlp(" ".join(lemma)) if token.pos_.startswith(("NOUN", "VERB", "ADJ"))]
    datos = palabras_con_peso + palabras_no_vacias
    fin = list(set(datos))
    mensaje = f"*****titulo*****\n{keyargs['texto']}\n{fin}"
    print(mensaje)
    return fin
  
def prueba():
  doc = ["peliculas", "peliculas"]
  doc2 = ["de", "de"]
  doc3 = ["mierda"]
  
  fin = [token.lemma_ for token in nlp(" ".join(list(doc) + list(doc2) + list(doc3)))]
  print(fin)
  
prueba()