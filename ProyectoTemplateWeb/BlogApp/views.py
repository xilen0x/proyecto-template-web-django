from django.shortcuts import render
from BlogApp.models import Post #importo la clase Post del archivo models de mi app.

# Create your views here.
def blog(request):
        
    var_post = Post.objects.all() #importo todos los objetos de la clase Servicio
    return render(request, "blog/blog.html", {"posts": var_post}) #para q muestre los servicios