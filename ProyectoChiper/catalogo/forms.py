from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'foto',
            'nombre',
            'precio',
            'tipo',
            'catalogo',
          #  'inventario',
        ]

        labels = {
            'foto' : 'Foto',
            'nombre' : 'Nombre',
            'precio' : 'Precio',
            'tipo' : 'Tipo',
            'catalogo':'Catalogo',
           # 'inventario':'Inventario',
        }