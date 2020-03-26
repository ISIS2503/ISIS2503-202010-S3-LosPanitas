from django.shortcuts import render
from django.shortcuts import render
from .forms import ProductoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .catalogo_logic.catalogo_logic import get_catalogo, create_producto
from django.contrib.auth.decorators import login_required

@login_required
def catalogo_list(request):
    catalogo = get_catalogo()
    context = {
        'catalogo_list': catalogo
    }
    return render(request, 'Catalogo/catalogo.html', context)

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            create_producto(form)
            messages.add_message(request, messages.SUCCESS, 'Producto create successful')
            return HttpResponseRedirect(reverse('productoCreate'))
        else:
            print(form.errors)
    else:
        form = ProductoForm()

    context = {
        'form': form,
    }

    return render(request, 'Measurement/measurementCreate.html', context)
