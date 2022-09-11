from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.tienda, name="tienda"),
  path('carrito/', include("carrito.urls"), name="urls_carrito"),
  path('<cat>/', views.categoria, name="categoria"),
  path('<cat>/<producto>/', views.producto, name="producto"),
]
