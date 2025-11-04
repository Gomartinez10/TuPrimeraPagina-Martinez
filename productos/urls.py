from django.urls import path
from productos.views import *

urlpatterns = [
    path('crear/', ArticuloCreateView.as_view(), name='articulo_crear'),
    path('', ArticuloListView.as_view(), name='articulo_lista'),
    path('<int:pk>/', ArticuloDetailView.as_view(), name='articulo_detalle'),
    path('<int:pk>/editar/', ArticuloUpdateView.as_view(), name='articulo_editar'),
    path('<int:pk>/eliminar/', ArticuloDeleteView.as_view(), name='articulo_eliminar'),
]