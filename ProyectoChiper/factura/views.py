from django.shortcuts import render
from .logic.logic_facturas import  get_all_facturas
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def get_facturas(request):
    facturas = get_all_facturas()
    facturas_list = serializers.serialize('json', facturas)
    return HttpResponse(facturas_list,
                        content_type='application/json')