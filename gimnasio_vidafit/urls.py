from django.urls import path
from gimnasio_vidafit.views import *

urlpatterns = [
    path("", index , name="index"),
    path("registro/", registro, name="registro"),
    path("registro_profesional/", registro_profesional, name="registro_profesional"),
    path("agendar_clases/", agendar_clase, name= "agendar_clase")
    
]