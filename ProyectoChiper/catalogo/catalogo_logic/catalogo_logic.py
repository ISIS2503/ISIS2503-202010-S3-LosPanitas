from django.db import models
from ..models import Catalogo

#ASR1
def get_catalogo():
    queryset=Catalogo.objects.all()
    return (queryset)

#ASR2
def create_producto(form):
    #FALTAVERIFICAR
    producto=form.save()
    producto.save()
    return ()

