from cProfile import label
from django import forms

class FormContacto(forms.Form):
  nombre = forms.CharField(label="Nombre", max_length=50)
  correo = forms.EmailField(label="Correo electrónico", max_length=100)
  mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea)