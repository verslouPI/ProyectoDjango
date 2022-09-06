from django.contrib import admin
from servicios.models import Servicio

# Register your models here.

@admin.register(Servicio)
class ServiciosAdmin(admin.ModelAdmin):

  #Muestra en solo lectura los campos de created y updated cuando se va hacer un nuevo registro
  readonly_fields = ("created","updated");

  #Muestra solo los datos de la tupla en la tabla servicios de la pagina admin
  list_display = ("id","titulo","contenido", "show_image","created", "updated")

  #Permite hacer busquedas del libro por esos campos en la pagina admin
  search_fields = ("titulo", "created", "updated")

  #Permite filtrar los datos por los campos dados en la pagina admin
  list_filter = ("created", "updated")

  #agrega una barra arriba con años, meses y dias disponibles en la tabla
  date_hierarchy = "created"
