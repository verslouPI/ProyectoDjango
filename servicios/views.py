from django.shortcuts import render

from .models import Servicio

# Create your views here.

def servicios(request):

  #La intruccion trae todos los registros que estan en el modelo Servicio, como si hiciera un SELECT * FROM Servicio
  servicios = Servicio.objects.all()
  return render(request, "servicios/servicios.html", {"servicios":servicios})