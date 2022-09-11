from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Categoria, Producto

# Create your views here.


def tienda(request: HttpRequest) -> HttpResponse:
  categorias = Categoria.objects.all()
  productos = Producto.objects.all()
  return render(request, "tienda/tienda.html", {"categorias":categorias, "productos":productos})

def categoria(request: HttpRequest, cat: str) -> HttpResponse:
  cat = cat.capitalize()
  categorias = Categoria.objects.all()
  try:
    categoria = Categoria.objects.get(categoria=cat)
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, "tienda/categoria.html", {"categoria":cat, "categorias":categorias, "productos":productos})
  except Categoria.DoesNotExist:
    return render(request, "tienda/errors/noCategoria.html", {"categorias":categorias})

def producto(request: HttpRequest, cat: str, producto: str) -> HttpResponse:
  try:
    cat = cat.capitalize()
    idProducto = int(producto)
    categorias = Categoria.objects.all()
    producto = Producto.objects.get(id=idProducto)
    categoria = Categoria.objects.get(categoria=cat)
    productosRelacionados = Producto.objects.filter(categoria=categoria).exclude(id=idProducto)[:5]
    if str(producto.categoria) == cat:
      return render(request, "tienda/detalleProducto.html", {"categorias":categorias, "producto":producto, "productos": productosRelacionados})
    raise Producto.DoesNotExist

  except Producto.DoesNotExist:
    return render(request, "tienda/errors/noProducto.html", {"categorias":categorias})

  except Exception:
    return render(request, "tienda/errors/general.html", {"categorias":categorias})
