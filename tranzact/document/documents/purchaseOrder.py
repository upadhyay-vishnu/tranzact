from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry


from ..models import PurchaseOrder

@registry.register_document
class PurchaseOrderDocument(Document):
    class index:
        name = 'purchase_order'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 1}

    class Django:
        model = PurchaseOrder
        