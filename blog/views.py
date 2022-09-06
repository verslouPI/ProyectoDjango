from unicodedata import category
from django.shortcuts import render
from .models import Post, Categoria
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse

# Create your views here.

def get_categorias():
    categorias = set()
    for post in Post.objects.all():
      for cat in post.categoria.all():
        categorias.add(cat)
    return categorias

class Blog:

  _posts = None
  _categorias = None

  @classmethod
  def blog(cls, request):
    cls._categorias = get_categorias()
    cls._posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts":cls._posts, "categorias":cls._categorias})

  @classmethod
  def categoria(cls, request: HttpRequest, cat: str) -> HttpResponse:
    cls._categorias = get_categorias()
    cat = cat.capitalize()
    cat_de_los_posts = Categoria.objects.get(categoria=cat)
    posts_de_esa_categoria = Post.objects.filter(categoria=cat_de_los_posts)

    return  render(request, "blog/categorias.html", {"categoria":cat_de_los_posts,"posts":posts_de_esa_categoria, "categorias": cls._categorias})