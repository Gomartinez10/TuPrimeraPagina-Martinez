from django import forms
from Sedes.models import *


class SedeForm(forms.ModelForm):
    class Meta:
        model = Sede
        fields = ["nombre","calle","altura"]
        widgets = {
                "nombre": forms.TextInput(attrs={"class": "form-control"}),
                "calle": forms.TextInput(attrs={"class": "form-control"}),
                "altura": forms.TextInput(attrs={"class": "form-control"}),
        }
    