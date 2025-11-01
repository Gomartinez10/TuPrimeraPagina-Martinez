from django.shortcuts import render
from Sedes.forms import SedeForm 
from Sedes.models import Sede
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView


class SedeListView(ListView):
    model = Sede
    template_name = "Sedes/sedes_list.html"
    context_object_name = "sedes"

    def get_queryset(self):
        query = self.request.GET.get("q", "").strip() 
        if query:
            return Sede.objects.filter(nombre__icontains=query) 
        return Sede.objects.all().order_by('nombre') 



class SedeCreateView(CreateView):
    model = Sede
    form_class = SedeForm
    template_name = "Sedes/sedes_form.html"
    success_url = reverse_lazy("sede_list")
    

class SedeUpdateView(UpdateView):
    model = Sede
    form_class = SedeForm
    template_name = "Sedes/sedes_form.html"
    success_url = reverse_lazy("sede_list")
    slug_field = "altura"
    pk_url_kwarg = "altura" 
    
    
class SedeDeleteView(DeleteView):
    model = Sede
    template_name = "Sedes/sede_delete.html"
    success_url = reverse_lazy("sede_list")
    slug_field = "altura"
    pk_url_kwarg = "altura" 
    
    
class SedeDetailView(DetailView):
    model = Sede
    template_name = "Sedes/sede_detail.html"
    context_object_name = "sede"
    slug_field = "calle"         
    slug_url_kwarg = "calle" 
