from django import forms
from .models import Cita


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            "nombre_cliente",
            "email_cliente",
            "barbero",
            "servicio",
            "fecha",
            "hora",
        ]
