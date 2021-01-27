''' Archivo url q afecta solo a esta app '''

from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('servicios/', views.servicios, name="Servicios"),
    path('tienda/', views.tienda, name="Tienda"),
    path('blog/', views.blog, name="Blog"),
    path('contacto/', views.contacto, name="Contacto"),
]