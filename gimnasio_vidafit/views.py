from django.shortcuts import render, redirect
from gimnasio_vidafit.forms import *
from gimnasio_vidafit.models import Profesional

def index(request):
    return render(request, "gimnasio_vidafit/index.html")
    
def registro(request):
    if request.method == "POST":
        form = AsociadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AsociadoForm()
            
    return render(request,"gimnasio_vidafit/registro.html", {"form": form})


def registro_profesional(request):
    if request.method == "POST":
        form = ProfesionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ProfesionalForm()
            
    return render(request,"gimnasio_vidafit/registro_profesional.html", {"form": form})



def agendar_clase(request):
    if request.method == "POST":
        form = ClasesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ClasesForm()
        
    return render(request,"gimnasio_vidafit/agendar_clases.html", {"form":form})


def buscar_profesor(request):
    query = request.GET.get("q","")
    if len(query) > 0:
        profesor = Profesional.objects.filter(nombre__icontains=query).order_by("-apellido")
    else:
        profesor = Profesional.objects.all().order_by("-apellido")
    return render(request,"gimnasio_vidafit/buscar_profesor.html",{"asociado": profesor, "query": query})