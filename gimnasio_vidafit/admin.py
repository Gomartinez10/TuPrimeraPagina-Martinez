from django.contrib import admin

from gimnasio_vidafit.models import *

@admin.register(Asociado)
class AsociadoAdmin(admin.ModelAdmin):
    list_display = ("nombre","apellido","email")
    list_display_links = ("nombre","apellido")
    search_fields = ("nombre","apellido")
    list_filter = ("fecha_de_nacimiento",)
    ordering = ("apellido","nombre")
