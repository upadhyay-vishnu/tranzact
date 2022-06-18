from django.db import models

from common import constants
from customer import models as customer_models
from common.models import BaseModel, Document, Company
from product.models import SourceProduct, ConsumerProduct

class TNC(Document):
    tnc_type = models.CharField(max_length=50, choices=constants.Document.choices)
    version = models.SmallIntegerField()


class PurchaseOrder(Document):
    cutomer = models.ForeignKey(customer_models.Customer, on_delete=models.CASCADE)
    n_source = models.ForeignKey(customer_models.NSource, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    rate = models.FloatField()
    delivery_date = models.DateTimeField()
    tnc = models.ForeignKey(TNC, on_delete=models.CASCADE)
    doc_type = models.CharField(max_length=50, choices=constants.Document.choices)
    product = models.ForeignKey(SourceProduct, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cutomer.name}-{self.n_source.name}-{self.product}'


class InwardDocument(Document):
    doc_type = models.CharField(max_length=50, choices=constants.Document.choices)
    cutomer = models.ForeignKey(customer_models.Customer, on_delete=models.CASCADE)
    n_source = models.ForeignKey(customer_models.NSource, on_delete=models.CASCADE)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(SourceProduct, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cutomer.name}-{self.n_source.name}-{self.purchase_order.id}'


class OrderConfirmation(Document):
    doc_type = models.CharField(max_length=50, choices=constants.Document.choices)
    cutomer = models.ForeignKey(customer_models.Customer, on_delete=models.CASCADE)
    n_client = models.ForeignKey(customer_models.NClient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    rate = models.PositiveIntegerField()
    delivery_date = models.DateTimeField()
    tnc = models.ForeignKey(TNC, on_delete=models.CASCADE)
    product = models.ForeignKey(SourceProduct, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}-{self.cutomer.name}-{self.n_client.name}-{self.delivery_date}'


class Invoice(Document):
    doc_type = models.CharField(max_length=50, choices=constants.Document.choices)
    cutomer = models.ForeignKey(customer_models.Customer, on_delete=models.CASCADE)
    n_client = models.ForeignKey(customer_models.NClient, on_delete=models.CASCADE)
    order = models.ForeignKey(OrderConfirmation, on_delete=models.CASCADE)
    product = models.ForeignKey(SourceProduct, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}-{self.cutomer.name}-{self.n_client.name}-{self.order.id}'


class SalesQuotation(Document):
    doc_type = models.CharField(max_length=50, choices=constants.Document.choices)
    cutomer = models.ForeignKey(customer_models.Customer, on_delete=models.CASCADE)
    n_client = models.ForeignKey(customer_models.NClient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    rate = models.FloatField()
    tnc = models.ForeignKey(TNC, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}-{self.cutomer.name}-{self.n_client.name}'

