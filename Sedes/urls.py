from django.urls import path
from Sedes.views import *


urlpatterns = [
    path('', SedeListView.as_view(), name='sede_list'),
    path('nueva/', SedeCreateView.as_view(), name='sede_create'),
    path('sede/editar/<uuid:codigo>/', SedeUpdateView.as_view(), name='sede_edit'),
    path('sede/eliminar/<uuid:codigo>/', SedeDeleteView.as_view(), name='sede_delete'),
    path('sede/<str:calle>/', SedeDetailView.as_view(), name='sede_detail'),
]