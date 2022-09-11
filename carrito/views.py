from math import prod
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from tienda.models import Producto, Categoria
from .carro import Carro


# Create your views here.

def carrito(request: HttpRequest) -> HttpResponse:
    categorias = Categoria.objects.all()
    return render(request, "tienda/carrito.html", {"categorias": categorias})

def agregar_productos(request: HttpRequest, idProducto: int) -> HttpResponse:
  
  try:
    carrito = Carro(request)
    producto = Producto.objects.get(id=idProducto)
    cantidad = request.POST.get("numProducto")
    categorias = Categoria.objects.all()
    carrito.agregar(producto=producto, cantidad=int(cantidad))
    return redirect("producto", cat=str(producto.categoria).lower(), producto=str(producto.id))
  
  except ValueError:
    return render(request, "tienda/errors/noNumber.html", {"categorias":categorias})
  
  except Producto.DoesNotExist:
    return render(request, "tienda/errors/noProducto.html", {"categorias":categorias})


def sumar_producto(request: HttpRequest, idProducto: int) -> HttpResponse:
  carrito = Carro(request)
  producto = Producto.objects.get(id=idProducto)
  carrito.sumar(producto=producto)

  return redirect("carro:carrito")


def restar_producto(request: HttpRequest, idProducto: int) -> HttpResponse:
  
  carrito = Carro(request)
  producto = Producto.objects.get(id=idProducto)
  carrito.restar(producto=producto)

  return redirect("carro:carrito")


def eliminar_producto(request: HttpRequest, idProducto: str) -> HttpResponse:
  
  carrito = Carro(request)
  producto = Producto.objects.get(id=idProducto)
  carrito.eliminar(producto=producto)

  return redirect("carro:carrito")


def limpiar_carro(request: HttpRequest) -> HttpResponse:
  
  carrito = Carro(request)
  carrito.limpiar()

  return redirect("carro:carrito")