from django.urls import path
from gimnasio_vidafit.views import index

urlpatterns = [
    path("", index , name="index"),
    
]