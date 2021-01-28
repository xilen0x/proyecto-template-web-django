from django.contrib import admin
from .models import Servicio #importo el modelo creado

# Register your models here.

#esta clase es para q aparezca en el menu de admin los campos created y updated del archivo models.py
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

#con esta línea (mas la importación arriba de la clase Servicio del archivo models), logramos q aparezca en nuestro admin el item Servicios.
admin.site.register(Servicio, ServicioAdmin)