''' Archivo url q afecta solo a esta app '''

from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('servicios/', views.servicios, name="Servicios"),
    path('tienda/', views.tienda, name="Tienda"),
    path('blog/', views.blog, name="Blog"),
    path('contacto/', views.contacto, name="Contacto"),
]

# AGREGAMOS UNA URL PARA LAS IMAGENES: (Ademas de las importaciones arriba 'from django.conf import settings' y 'from django.conf.urls.static import static')
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)