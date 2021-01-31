from django.shortcuts import render
from BlogApp.models import Post, Categoria #importamos las clases del archivo models de mi app, q utilizaremos.

# Create your views here.
def blogView(request):
        
    var_post = Post.objects.all() #importo todos los objetos de la clase Servicio
    return render(request, "blog/blog.html", {"posts": var_post}) #para q muestre los servicios

def categoriaView(request, categoria_id):
    var_categoria = Categoria.objects.get(id=categoria_id)
    var_post = Post.objects.filter(categorias=var_categoria)
    return render(request, "blog/categorias.html", {'categoria':var_categoria, "posts": var_post})
