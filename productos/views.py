from django.shortcuts import render
from productos.forms import ArticuloForm
from productos.models import Articulo
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.shortcuts import get_object_or_404


class ArticuloListView(ListView):
    model = Articulo
    context_object_name = 'articulos'
    template_name = 'productos/lista_articulo.html' 


class ArticuloDetailView(DetailView):
    model = Articulo
    context_object_name = 'articulo'
    template_name = 'productos/detalle_articulo.html'


class ArticuloCreateView(CreateView):
    model = Articulo
    form_class = ArticuloForm 
    template_name = 'productos/form_articulo.html' 
    success_url = reverse_lazy('articulo_lista')

class ArticuloUpdateView(UpdateView):
    model = Articulo
    form_class = ArticuloForm 
    template_name = 'productos/form_articulo.html'
    
    def get_success_url(self):
        return reverse_lazy('articulo_detalle', kwargs={'pk': self.object.pk})

class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name = 'productos/eliminar_articulo.html'
    success_url = reverse_lazy('articulo_lista')