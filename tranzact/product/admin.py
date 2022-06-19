from django.contrib import admin

# Register your models here.
from .models import SourceProduct, ConsumerProduct

@admin.register(ConsumerProduct)
class ConsumerProductAdmin(admin.ModelAdmin):
	pass


@admin.register(SourceProduct)
class SourceProductAdmin(admin.ModelAdmin):
	pass


