from django.db import models

from common import constants
from common import models as c_models


class Customer(c_models.Company):
	customer_type = models.CharField(max_length=50, choices=constants.Company.choices)
	product = models.CharField(max_length=50, choices=constants.Product.choices)

	def __str__(self):
		return f'{self.customer_type}: {self.prdouct}'

class NSource(c_models.Company):	
	customer_type = models.CharField(max_length=50, choices=constants.Company.choices)
	product = models.CharField(max_length=50, choices=constants.Product.choices)

	def __str__(self):
		return f'{self.customer_type}: {self.prdouct}'


class NClient(c_models.Company):	
	customer_type = models.CharField(max_length=50, choices=constants.Company.choices)
	product = models.CharField(max_length=50, choices=constants.Product.choices)

	def __str__(self):
		return f'{self.customer_type}: {self.prdouct}'


