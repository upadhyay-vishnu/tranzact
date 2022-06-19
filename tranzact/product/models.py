from django.db import models

# Create your models here.
from common.models import Product
from customer.models import Customer, NClient, NSource

class SourceProduct(Product):
	ns_client = models.ForeignKey(NSource, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.ns_client.name}-{self.customer.name}'

class ConsumerProduct(Product):
	nc_client = models.ForeignKey(NClient, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.nc_client.name}-{self.customer.name}'
