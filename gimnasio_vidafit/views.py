from django.shortcuts import render, redirect, get_object_or_404
from gimnasio_vidafit.forms import *
from gimnasio_vidafit.models import Profesional
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

@login_required
def registro_profesional(request):
    if request.method == "POST":
        form = ProfesionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ProfesionalForm()
            
    return render(request,"gimnasio_vidafit/registro_profesional.html", {"form": form})


@login_required
def agendar_clase(request):
    if request.method == "POST":
        form = ClasesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ClasesForm()
        
    return render(request,"gimnasio_vidafit/agendar_clases.html", {"form":form})

@login_required
def buscar_profesor(request):
    query = request.GET.get("q","")
    if len(query) > 0:
        profesor = Profesional.objects.filter(nombre__icontains=query).order_by("-apellido")
    else:
        profesor = Profesional.objects.all().order_by("-apellido")
    return render(request,"gimnasio_vidafit/buscar_profesor.html",{"asociado": profesor, "query": query})

@login_required
def eliminar_profesor(request,legajo):
    profesional = get_object_or_404(Profesional, legajo=legajo)
    profesional.delete()
    messages.success(request,"Profesional eliminado con éxito.")
    return redirect(buscar_profesor)
    
@login_required   
def editar_profesor(request,legajo):
    profesional = get_object_or_404(Profesional,legajo=legajo)
    if request.method == "POST":
        form = ProfesionalForm(request.POST, instance=profesional)
        if form.is_valid():
            form.save()
            return redirect(buscar_profesor)   
    else:
        form = ProfesionalForm(instance=profesional)
        
    return render(request, "gimnasio_vidafit/registro_profesional.html", {"form": form, "edicion": True})


from django.shortcuts import render

def about_me(request):
    return render(request, 'gimnasio_vidafit/about_me.html')