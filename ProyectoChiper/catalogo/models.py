from django.db import models

class Catalogo(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % (self.nombre)