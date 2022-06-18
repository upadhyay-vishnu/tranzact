from django.contrib import admin

# Register your models here.
from .models import Customer, NClient, NSource

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	pass


@admin.register(NClient)
class NClientAdmin(admin.ModelAdmin):
	pass


@admin.register(NSource)
class NSourceAdmin(admin.ModelAdmin):
	pass
