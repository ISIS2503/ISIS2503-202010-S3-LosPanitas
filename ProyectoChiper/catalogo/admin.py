from django.contrib import admin
from .models import Catalogo, Producto, Cantidad

admin.site.register(Catalogo)
admin.site.register(Producto)
admin.site.register(Cantidad)
