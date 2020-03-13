from django.db import models
from catalogo.models import Catalogo

class Producto(models.Model):
    foto = models.CharField(max_length=100)
    nombre = models.CharField(max_length=30)
    precio = models.FloatField(null=True, blank=True, default=None)
    tipo = models.CharField(max_length=20)
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return '%s-%s-%s' % (self.nombre, self.precio, self.catalogo)




