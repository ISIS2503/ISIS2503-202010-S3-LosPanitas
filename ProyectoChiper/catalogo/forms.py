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
        ]

        labels = {
            'foto' : 'Foto',
            'nombre' : 'Nombre',
            'precio' : 'Precio',
            'tipo' : 'Tipo',
        }