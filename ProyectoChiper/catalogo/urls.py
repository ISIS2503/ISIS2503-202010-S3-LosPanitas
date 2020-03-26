from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('catalogo/', views.catalogo_list),
    path('productocreate/', csrf_exempt(views.producto_create), name='productoCreate'),
]