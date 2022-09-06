from django.urls import path
from blog import views
urlpatterns = [
  path('', views.Blog.blog, name="blog"),
  path('categoria/<cat>/', views.Blog.categoria, name="categoria"),
]
