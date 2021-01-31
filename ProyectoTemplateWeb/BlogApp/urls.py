from django.urls import path
from . import views

urlpatterns = [

    path('', views.blogView, name="Blog"),
    path('categoria/<categoria_id>/', views.categoriaView, name="categoria"),
]