from ..models import Factura


def get_all_facturas():
    facturas = Factura.objects.all()
    return facturas
