from django.db import models
from catalogo.models import Producto

# Create your models here.
class Factura(models.Model):
    fecha = models.DateTimeField(auto_now_add=False)
    monto = models.FloatField()

    def __str__(self):
        return '%s %s'.format(self.fecha, self.monto)
