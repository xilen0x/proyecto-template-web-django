from django.shortcuts import render
from ServiciosApp.models import Servicio #importo la clase Servicio del archivo models de mi app.

# Create your views here.

def servicios(request):
    
    mis_servicios = Servicio.objects.all() #importo todos los objetos de la clase Servicio
    return render(request, "servicios/servicios.html", {"servicios": mis_servicios}) #para q muestre los servicios