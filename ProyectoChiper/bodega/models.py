from django.db import models

class Proveedor(models.Model):

    id=models.FloatField(null=False, blank=False, default=None, primary_key=True)
    nombre = models.CharField(max_length=30)

    def _str_(self):
        return '%s' % (self.nombre)


class ProductoProveedor(models.Model):

    foto = models.CharField(max_length=100)
    nombre = models.CharField(max_length=30)
    cant = models.FloatField(null=True, blank=False, default=None)
    fechaLlegada=models.DateTimeField(auto_now=False, auto_now_add=True)
    provid=models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def _str_(self):
        return '%s' % (self.nombre)


class InventarioBodega(models.Model):
    id = models.FloatField(null=False, blank=False, default=None, primary_key=True)

    def _str_(self):
        return '%s' % (self.id)