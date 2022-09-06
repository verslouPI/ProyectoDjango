from django.contrib import admin
from blog.models import Categoria, Post

# Register your models here.


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
  readonly_fields = ("created","updated")
  list_display = ("id_categoria", "categoria")
  search_fields = ("id_categoria", "categoria")
  list_filter = ("created","updated")
  date_hierarchy = "created"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  readonly_fields = ("created","updated")
  list_display = ("id_post", "titulo", "contenido", "show_image", "autor")
  search_fields = ("id_post", "titulo", "autor", "categoria")
  list_filter = ("created","updated")
  date_hierarchy = "created"
