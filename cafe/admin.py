from django.contrib import admin
from .models import Item,Order,Category
# Register your models here.

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Category)