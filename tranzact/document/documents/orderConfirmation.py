from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry


from ..models import OrderConfirmation

@registry.register_document
class SalesQuotationDocument(Document):
    class index:
        name = 'order_confirmation'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 1}

    class Django:
        model = OrderConfirmation