from django import forms
from gimnasio_vidafit.models import Asociado , Profesional , Clases

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
        
        
class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = ["nombre", "apellido","email", "fecha_de_nacimiento","especialidad","legajo"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "especialidad": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_de_nacimiento": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "legajo": forms.NumberInput(attrs={"class": "form-control"}),
        }
        
        
        
class ClasesForm(forms.ModelForm):
    class Meta:
        model = Clases
        fields = ["nombre","fecha"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "fecha": forms.DateInput(attrs={"type": "date", "class": "form-control"})
        }
                                                    