from django.shortcuts import render, HttpResponse
from ServiciosApp.models import Servicio #importo la clase Servicio del archivo models de mi app.

# Create your views here.

def inicio(request):

    return render(request, "ProyectoWebApp/inicio.html")


def servicios(request):
    
    mis_servicios = Servicio.objects.all() #importo todos los objetos de la clase Servicio
    return render(request, "ProyectoWebApp/servicios.html", {"servicios": mis_servicios}) #para q muestre los servicios


def tienda(request):
    
    return render(request, "ProyectoWebApp/tienda.html")

def blog(request):
    
    return render(request, "ProyectoWebApp/blog.html")

def contacto(request):
    
    return render(request, "ProyectoWebApp/contacto.html")