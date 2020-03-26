from django.db import models
from ..models import Catalogo
from ..models import Producto


#ASR1
def get_catalogo():
    queryset=Producto.objects.all()
    return (queryset)

#ASR2
def create_producto(form):
    #FALTAVERIFICAR
    producto=form.save()
    producto.save()
    return ()

