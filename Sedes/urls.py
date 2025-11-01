from django.urls import path
from Sedes.views import *


urlpatterns = [
    path("",SedeListView.as_view(), name ="sede_list"),
    path("nueva/",SedeCreateView.as_view(), name = "sede_create"),
    path("<str:calle>/", SedeDetailView.as_view(), name = "sede_detail"),
    path("<int:altura>/editar/", SedeUpdateView.as_view(), name="sede_edit"),
    path("<int:altura>/eliminar/", SedeDeleteView.as_view(), name = "sede_delete"),
    
    
]