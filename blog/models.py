from django.db import models
from helpers import path_file_name, generate_uuid
from django.contrib.auth.models import User
from django.utils.html import mark_safe
import uuid

# Create your models here.

class Categoria(models.Model):

  class Meta:
    verbose_name = "catergoria"
    verbose_name_plural = "categorias"

  #UUIDField Producira un codigo irrepetible de tamaño uuid(o char32), nos servira de id
  #UUIDField no crea id solo por ello podemos usar la libreria uuid con  alguno de susu algoritmos y crear un id o crear una funcion nosotros mismos en este caso.
  #editable=False hace que el campo no se muestre en el administrador y no se pueda editar
  id_categoria = models.CharField(max_length=8,primary_key=True, default=generate_uuid,editable=False)
  categoria = models.CharField(max_length=20)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.categoria

"""
def path_file_name(instance, filename):
  filename, ext = os.path.splitext(filename)
  return "%s/%s%s" % ("blog", uuid.uuid4(), ext)
"""
class Post(models.Model):

  class Meta:
    verbose_name = "post"
    verbose_name_plural = "posts"

  def show_image(self):
    return mark_safe("<a href='/media/%s' target='_blank'><img src='/media/%s' width='75px' height='50'></a>" % (self.imagen, self.imagen))

  id_post = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  titulo = models.CharField(max_length=100)
  contenido = models.CharField(max_length=800)
  imagen = models.ImageField(upload_to=path_file_name("blog"), null=True, blank=True)
  autor = models.ForeignKey(User, default=2,on_delete=models.SET_DEFAULT)
  categoria = models.ManyToManyField(Categoria)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return self.titulo