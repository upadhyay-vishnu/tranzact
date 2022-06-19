from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry


from ..models import TnC

@@egistry.register_document
class TnCDocument(Document):
    class index:
        name = 'tnc'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 1}

    class Django:
        model = TnC
        