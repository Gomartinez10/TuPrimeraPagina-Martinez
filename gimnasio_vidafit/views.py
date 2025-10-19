from django.shortcuts import render, redirect
from gimnasio_vidafit.forms import *

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
        form = AsociadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AsociadoForm()
            
    return render(request,"gimnasio_vidafit/registro_profesional.html", {"form": form})