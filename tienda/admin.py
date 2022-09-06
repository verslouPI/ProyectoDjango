from telnetlib import SE
from typing import Sequence
from django.contrib import admin
from tienda.models import Categoria, Proveedor, Producto

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
  readonly_fields: Sequence[str] = ("created","updated")
  list_display: Sequence[str] = ("id","categoria","descripcion","show_image","created","updated")
  search_fields: Sequence[str] = ("id","categoria")
  list_filter: Sequence[str] = ("created", "updated")

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
  readonly_fields: Sequence[str] = ("created", "updated")
  list_display: Sequence[str] = ("id", "proveedor", "created","updated")
  search_fields: Sequence[str] = ("id", "proveedor")
  list_filter: Sequence[str] = ("created","updated")

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
  readonly_fields: Sequence[str] = ("created","updated")
  list_display: Sequence[str] = ("id", "codigo","producto", "descripcion", "categoria", "show_image", "precio", "disponibilidad", "proveedor", "created", "updated")
  search_fields: Sequence[str] = ("id", "producto")
  list_filter: Sequence[str] = ("created", "updated")