''' Archivo url q afecta solo a esta app '''

from django.urls import path
from . import views #importamos las views desde el mismo directorio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.servicios, name="Servicios"),
]