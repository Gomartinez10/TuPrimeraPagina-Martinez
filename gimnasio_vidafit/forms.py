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
        
        

ESPECIALIDADES = [
    ('yoga', 'Yoga'),
    ('natacion', 'Natación'),
    ('musculacion', 'Musculación'),
]

class ProfesionalForm(forms.ModelForm):
    especialidad = forms.ChoiceField(
        choices=[('', 'Seleccione una especialidad')] + ESPECIALIDADES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False
    )

    class Meta:
        model = Profesional
        fields = ['nombre', 'apellido', 'email', 'especialidad', 'fecha_de_nacimiento', 'legajo']
        widgets = {
            'fecha_de_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'legajo': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        edicion = kwargs.pop('edicion', False)
        super().__init__(*args, **kwargs)
        if edicion:
            self.fields.pop('legajo', None)  # No mostrar legajo en edición
        else:
            self.fields['legajo'].widget.attrs['required'] = True
        
        
        
class ClasesForm(forms.ModelForm):
    class Meta:
        model = Clases
        fields = ["nombre","fecha"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "fecha": forms.DateInput(attrs={"type": "date", "class": "form-control"})
        }
                                                    