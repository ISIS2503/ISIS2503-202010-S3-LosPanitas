from django.shortcuts import render
from .logic.logic_facturas import  get_all_facturas
from django.http import HttpResponse
from django.core import serializers
from .logic.logic_facturas import get_all_productosFactura
from .forms import ProductoFacturaForm
from .logic.logic_facturas import add_producto
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import ProductoFactura

# Create your views here.
def facturas(request):

    prods=get_all_productosFactura()

    gerente = False
    context = {
        'prod_list': prods,
        'gerente': gerente,
    }
    return render(request, 'createFactura.html', context)

def add_prod(request):
        if request.method == 'POST':
            form = ProductoFacturaForm(request.POST)
            if form.is_valid():
                rta=add_producto(form)
                if rta=='Producto creado':
                    messages.add_message(request, messages.SUCCESS, rta)
                    print(messages)
                    return HttpResponseRedirect(reverse('createFactura'))
                else:
                    messages.add_message(request, messages.ERROR, rta)
                    print(messages)
                    messages.error(request, "Error")
                    return HttpResponseRedirect(reverse('createFactura'))
            else:
                print(form.errors)
        else:
            form = ProductoFacturaForm()

        context = {
            'form': form,
        }

        return render(request, 'createFactura.html', context)