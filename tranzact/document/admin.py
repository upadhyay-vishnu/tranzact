from django.contrib import admin

# Register your models here.
from .models import TNC, PurchaseOrder,InwardDocument,OrderConfirmation,Invoice,SalesQuotation

@admin.register(TNC)
class TNCAdmin(admin.ModelAdmin):
	pass


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
	pass


@admin.register(InwardDocument)
class InwardDocumentAdmin(admin.ModelAdmin):
	pass


@admin.register(OrderConfirmation)
class OrderConfirmationOrderAdmin(admin.ModelAdmin):
	pass


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
	pass


@admin.register(SalesQuotation)
class SalesQuotationAdmin(admin.ModelAdmin):
	pass