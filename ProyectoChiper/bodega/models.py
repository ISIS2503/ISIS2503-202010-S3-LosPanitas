from django.db import models



class InventarioBodega(models.Model):
    id = models.FloatField(null=False, blank=False, default=None, primary_key=True)
