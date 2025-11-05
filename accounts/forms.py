from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import Perfil

class PerfilCreationForm(UserCreationForm):
    class Meta:
        model = Perfil
        fields = ("username", "email","avatar","fecha_de_nacimiento")
        
class PerfilChangeForm(UserChangeForm):
    class Meta:
        model = Perfil
        exclude = ("id",)
        