from django import forms
from .models import ProductoFactura

class ProductoFacturaForm(forms.ModelForm):
    class Meta:
        model = ProductoFactura
        fields = [
            'foto',
            'nombre',
            'precio',
            'tipo',
            'factura',
          #  'inventario',
        ]

        labels = {
            'foto' : 'Foto',
            'nombre' : 'Nombre',
            'precio' : 'Precio',
            'tipo' : 'Tipo',
            'factura':'Factura',
        }