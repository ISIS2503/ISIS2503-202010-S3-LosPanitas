from ..models import Factura
from ..models import ProductoFactura


def get_all_facturas():
    facturas = Factura.objects.all()
    return facturas

def get_all_productosFactura():
    productos = ProductoFactura.objects.all()
    return productos


def add_producto(form):
    nombreprod=form.cleaned_data.get('nombre')
    hello=''
    try:
        productico = ProductoFactura.objects.get(nombre=nombreprod)
        hello='Ya existe el producto'
    except ProductoFactura.DoesNotExist:
        productico=form.save()
        productico.save()
        hello='Producto creado'

    return hello
