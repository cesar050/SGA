from django import forms
from .models import Facultad, Carrera


class FacultadForm(forms.ModelForm):
    class Meta:
        model = Facultad
        fields = ['nombre', 'siglas']

class CarreraForm(forms.ModelForm):
    class Meta:
     model = Carrera
     fields = ['codigo', 'nombre', 'titulo', 'facultad', 'modalidad']
