from django.urls import path
from gimnasio_vidafit.views import index, registro

urlpatterns = [
    path("", index , name="index"),
    path("registro/", registro, name="registro")
]