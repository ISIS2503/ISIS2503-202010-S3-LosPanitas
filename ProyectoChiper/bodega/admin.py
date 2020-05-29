from django.contrib import admin
from .models import Proveedor, ProductoProveedor

admin.site.register(Proveedor)
admin.site.register(ProductoProveedor)