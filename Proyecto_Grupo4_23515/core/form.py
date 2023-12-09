from django import forms
from core.models import Alumno

class AlumnoForm(forms.ModelForm):
    
    nombre = forms.CharField(
        label=False,
        max_length=50,
        min_length=2,
        required=True,
        widget=forms.TextInput(attrs={"class": "inputsForm", "placeholder": "Nombre"}),
    )
    apellido = forms.CharField(
        label=False,
        max_length=50,
        min_length=2,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "inputsForm", "placeholder": "Apellido"}
        ),
    )
    dni = forms.CharField(
        label=False,
        max_length=50,
        min_length=2,
        required=True,
        widget=forms.NumberInput(
            attrs={"class": "inputsForm inputDni", "placeholder": "DNI"}
        ),
    )
    email = forms.CharField(
        label=False,
        max_length=50,
        min_length=2,
        required=True,
        widget=forms.EmailInput(attrs={"class": "inputsForm", "placeholder": "Email"}),
    )
    telefono = forms.CharField(
        label=False,
        max_length=50,
        min_length=2,
        required=True,
        widget=forms.TextInput(attrs={"class": "inputsForm", "placeholder": "Telefono"}),
    )

    class Meta:
        model = Alumno
        fields = [
            "nombre",
            "apellido",
            "dni",
            "email",
            "telefono",
        ]
