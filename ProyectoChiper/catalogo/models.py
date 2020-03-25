from django.db import models

from bodega.models import InventarioBodega


class Catalogo(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % (self.nombre)


class Producto(models.Model):
    foto = models.CharField(max_length=100)
    nombre = models.CharField(max_length=30)
    precio = models.FloatField(null=True, blank=True, default=None)
    tipo = models.CharField(max_length=20)
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE, default=None)
    inventario = models.ForeignKey(InventarioBodega, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return '%s-%s-%s' % (self.nombre, self.precio, self.catalogo)


class Cantidad(models.Model):
    cant = models.FloatField(null=True, blank=False, default=None)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)
