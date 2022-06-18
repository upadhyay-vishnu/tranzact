from django.db import models

# Create your models here.
from common.models import BaseModel
from product.models import SourceProduct, ConsumerProduct
from customer.models import Customer, NSource, NClient


class SourceProductPurchase(BaseModel):
	product = models.ForeignKey(SourceProduct, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	n_source = models.ForeignKey(NSource, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.product}-{self.n_source}-{self.customer}'


class ConsumerProductSell(BaseModel):
	product = models.ForeignKey(ConsumerProduct, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	n_client = models.ForeignKey(NClient, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.product}-{self.n_source}-{self.customer}'