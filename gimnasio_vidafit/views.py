from django.shortcuts import render

def index(request):
    return render(request, "gimnasio_vidafit/index.html")
    
