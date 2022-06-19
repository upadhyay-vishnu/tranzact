from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry


from .models import InwardDocument

@@registry.register_document
class InwardDocumentDocument(Document):
    def index():
        name = 'inward_document'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 1}

    class Django:
        model = InwardDocument