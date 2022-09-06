from ast import For
from smtplib import SMTPException
from django.shortcuts import render, redirect
from .forms import FormContacto
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def contacto(request):
  if request.method == "POST":
    form_contacto = FormContacto(request.POST)
    if form_contacto.is_valid():
      nombre = form_contacto.cleaned_data["nombre"]
      email = form_contacto.cleaned_data["correo"]
      mensaje = form_contacto.cleaned_data["mensaje"]

      try:
        send_mail(subject = f"Mensaje envido por: {nombre}", message=f"{mensaje} -> <b>Enviado desde {email}</b>",from_email=settings.EMAIL_HOST_USER,recipient_list=["negroek618@gmail.com", "jflav.nunez@gmail.com"])
        return redirect("/contacto/?validado=1")
      except Exception as error: #SMTPException as error:
        print(error)
        return redirect(f"/contacto/?validado=0")

  form_contacto = FormContacto()
  return render(request, "contacto/contacto.html", {"formulario":form_contacto})