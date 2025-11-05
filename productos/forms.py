from django import forms
from productos.models import *

class ArticuloForm(forms.ModelForm):
    class Meta: 
        model = Articulo
        fields = ['nombre', 'precio', 'descripcion', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
        
        