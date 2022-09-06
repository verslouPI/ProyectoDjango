from tabnanny import verbose
from django.db import models
from django.utils.html import mark_safe
from datetime import datetime
from helpers import path_file_name

# Create your models here.

class Servicio(models.Model):
  
  titulo = models.CharField(max_length=75)
  contenido = models.CharField(max_length=50)
  imagen = models.ImageField(upload_to=path_file_name("servicios"))
  created = models.DateField(auto_now_add=True) #auto_now_add agrega la fecha actual por default
  updated = models.DateField(auto_now_add=True)

  def show_image(self):
    return mark_safe("<a href='/media/%s' target='_blank'><img src='/media/%s' width='50px'></a>" % (self.imagen, self.imagen))

  class Meta:
    verbose_name = "servicio"
    verbose_name_plural = "servicios"
  
  def __str__(self):
    return self.titulo