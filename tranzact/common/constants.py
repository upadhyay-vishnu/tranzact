# -*- coding: utf-8 -*-
from django.db import models

class Company(models.TextChoices):
    CUSTOMER = "customer", "Customer"
    NSOURCE = "ns", "NS"
    NCLIENT = "nc", "NC"


class Document(models.TextChoices):
    PURCHASEORDER = "purchase_order", "PurchaseOrder"
    SALESQUOTE = "sales_quote", "SalesQuote"
    INVOICE = "invoice", "Invoice"
    ORDERCONFIRMATION = "order_confirmation", "OrderConfirmation"
    INWARDDOCUMENT = "inward_document", "InwardDocument"
    TNC = "tnc", "TnC"


class Product(models.TextChoices):
    STEEL = "Steel", "steel"
    SPRING = "Spring", "spring"
