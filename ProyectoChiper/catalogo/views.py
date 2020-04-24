from django.shortcuts import render
from django.shortcuts import render
from .forms import ProductoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .catalogo_logic.catalogo_logic import get_products, create_producto
from django.contrib.auth.decorators import login_required
from ProyectoChiper.auth0backend import getRole

#role = getRole(request)
#    if role == "Supervisor":


#@login_required
def catalogo_list(request):
    catalogo = get_products()
    context = {
        'catalogo_list': catalogo
    }
    return render(request, 'Catalogo/catalogo.html', context)

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            rta=create_producto(form)
            if rta=='Producto creado':
                messages.add_message(request, messages.SUCCESS, rta)
                print(messages)
                return HttpResponseRedirect(reverse('productoCreate'))
            else:
                messages.add_message(request, messages.ERROR, rta)
                print(messages)
                messages.error(request, "Error")
                return HttpResponseRedirect(reverse('productoCreate'))
        else:
            print(form.errors)
    else:
        form = ProductoForm()

    context = {
        'form': form,
    }

    return render(request, 'Catalogo/productoCreate.html', context)