from django.urls import path
from MyWEBI import views
urlpatterns = [
  path('', views.home, name="home"),
]
