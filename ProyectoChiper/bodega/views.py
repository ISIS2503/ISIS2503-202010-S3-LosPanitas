from django.shortcuts import render
from .bodega_logic.bodega_logic import get_prod_provall
from django.contrib.auth.decorators import login_required
from ProyectoChiper.auth0backend import getRole
# Create your views here


def prod_prov(request):

    prods=get_prod_provall()

    gerente = False
    context = {
        'prod_list': prods,
        'gerente': gerente,
    }
    return render(request, 'provprod.html', context)