from django.urls import path
from . import views

urlpatterns = [
    path('factura/', views.get_facturas, name='facturasList')
]

