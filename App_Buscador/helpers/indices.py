from elasticsearch_dsl import Document, Date, Integer, Keyword, Text, connections, Index, Integer
from App_Buscador.models import Contenido


my_index = Index('Contenido_index')


# Agrega el campo 'nombre' al índice
my_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@my_index.document
class ContenidoDocument(Document):
    id = Integer()
    titulo = Text(analyzer='spanish')
    categoria = Text(analyzer='spanish')
    generos = Text(analyzer='spanish')
    descripcion = Text(analyzer='spanish')

    class Index:
        name = 'contenido'

    class Django:
        model = Contenido

    def save(self, **kwargs):
        self.id = self.meta.id
        return super().save(**kwargs)

# Obtén todos los objetos del modelo
contenidos = Contenido.objects.all()

# Indexa los objetos en Elasticsearch
for contenido in contenidos:
    ContenidoDocument(
        titulo=contenido.titulo,
        categoria=contenido.categoria,
        generos=contenido.generos,
    ).save()


my_index.delete()

