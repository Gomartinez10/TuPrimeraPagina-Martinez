from django import forms
from gimnasio_vidafit.models import Asociado

class AsociadoForm(forms.ModelForm):
    class Meta:
        model = Asociado
        fields = ["nombre", "apellido","email", "fecha_de_nacimiento"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "fecha_de_nacimiento": forms.DateInput(attrs={"type": "date", "class": "form-control"})
        }