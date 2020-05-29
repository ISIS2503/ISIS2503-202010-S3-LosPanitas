from django.db import models
from catalogo.models import Producto

# Create your models here.
class Factura(models.Model):
    fecha = models.DateTimeField(auto_now_add=False)
    monto = models.FloatField()

class ProductoFactura(models.Model):
    foto = models.CharField(max_length=100, default="foto")
    nombre = models.CharField(max_length=30)
    precio = models.FloatField(null=True, blank=True, default=None)
    tipo = models.CharField(max_length=20)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s'.format(self.nombre, self.precio, self.tipo, self.factura)
