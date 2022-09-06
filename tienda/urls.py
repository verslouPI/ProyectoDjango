from django.urls import path
from . import views

urlpatterns = [
  path('', views.Tienda.tienda, name="tienda"),
  path('<cat>/', views.Tienda.categoria, name="categoria"),
  path('<cat>/<producto>/', views.Tienda.producto, name="producto"),
]
