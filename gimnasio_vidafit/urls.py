from django.urls import path
from gimnasio_vidafit.views import *

urlpatterns = [
    path("", index , name="index"),
    path("registro/", registro, name="registro"),
    path("registro_profesional/", registro_profesional, name="registro_profesional"),
    path("agendar_clases/", agendar_clase, name= "agendar_clase"),
    path("buscar_profesor/", buscar_profesor,name="buscar_profesor"),
    path("profesional/<int:legajo>/eliminar", eliminar_profesor, name="eliminar_profesor"),
    path("profesional/<int:legajo>/editar", editar_profesor, name= "editar_profesor"),
    
]