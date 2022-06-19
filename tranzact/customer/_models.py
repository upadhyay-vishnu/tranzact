from django.db import models

from common import constants
from common import models as c_models


class Customer(c_models.Company):
	customer_type = models.CharField(max_length=50, choices=constants.Company.choices)

	def __str__(self):
		return f'{self.name}-{self.customer_type}'

class NSource(c_models.Company):	
	customer_type = models.CharField(max_length=50, choices=constants.Company.choices)

	def __str__(self):
		return f'{self.name}-{self.customer_type}'


class NClient(c_models.Company):	
	customer_type = models.CharField(max_length=50, choices=constants.Company.choices)

	def __str__(self):
		return f'{self.name}-{self.customer_type}'


