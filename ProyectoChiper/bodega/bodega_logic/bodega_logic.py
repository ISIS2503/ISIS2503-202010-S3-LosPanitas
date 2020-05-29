from ..models import ProductoProveedor

#todos los productos por proveedor
def get_prod_provall():
    prods=ProductoProveedor.objects.all()
    return prods