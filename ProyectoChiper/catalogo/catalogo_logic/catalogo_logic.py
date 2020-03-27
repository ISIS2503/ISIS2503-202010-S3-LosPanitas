from django.db import models
from ..models import Catalogo
from ..models import Producto


def get_idcatalogo():
    catalogos= Catalogo.objects.get(nombre='CatalogoChiper').id
    return catalogos

# ASR1
def get_products():
    productos = Producto.objects.filter(catalogo=get_idcatalogo())
    return productos


# ASR2
def create_producto(form):
    nombreprod=form.cleaned_data.get('nombre')
    hello=''
    try:
        productico = Producto.objects.get(nombre=nombreprod)
        hello='Ya existe el producto'
    except Producto.DoesNotExist:
        productico=form.save()
        productico.save()
        hello='Producto creado'

    return hello

