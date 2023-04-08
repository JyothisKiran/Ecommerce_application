from django.contrib import admin
from .models import ShoeModel,Order,Cart,Brand

# Register your models here.

admin.site.register(ShoeModel)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Brand)