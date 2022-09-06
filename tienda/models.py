from distutils.command.upload import upload
from django.db import models
from helpers import generate_uuid, path_file_name
from django.utils.html import mark_safe
from django.utils import timezone

# Create your models here.


class Categoria(models.Model):
  categoria = models.CharField(max_length=50)
  imagen = models.ImageField(upload_to=path_file_name("tienda/categorias"), default="tienda/categorias/empty.jpg")
  descripcion = models.CharField(max_length=25, null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = "categoria"
    verbose_name_plural = "categorias"

  def show_image(self):
    return mark_safe("<a href='/media/%s' target='_blank'><img src='/media/%s' width='75' height='50'></a>" % (self.imagen, self.imagen))

  def __str__(self):
    return self.categoria


class Proveedor(models.Model):
  proveedor = models.CharField(max_length=50)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = "proveedor"
    verbose_name_plural = "proveedores"

  def __str__(self):
    return self.proveedor


class Producto(models.Model):
  codigo = models.CharField(max_length=9, default=generate_uuid)
  producto = models.CharField(max_length=50)
  descripcion = models.CharField(max_length=200)
  imagen = models.ImageField(upload_to=path_file_name("tienda/productos"),default="tienda/productos/empty.png")
  precio = models.DecimalField(max_digits=7, decimal_places=2)
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
  disponibilidad = models.IntegerField()
  proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)

  def show_image(self):
    return mark_safe("<a href='/media/%s' target='_blank'><img src='/media/%s' width='50' height='65'></a>" % (self.imagen, self.imagen))

  class Meta:
    verbose_name = "producto"
    verbose_name_plural = "productos"

  def __str__(self):
    return self.producto