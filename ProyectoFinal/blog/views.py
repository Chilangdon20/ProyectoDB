from django.shortcuts import render
from blog.models import Post,Categoria

# Create your views here.
# <img class="intro-img img-fluid mb-3 mb-lg-0 rounded" src="{{post.imagen.url}}" alt="" style="width: 50%;">
def blog(request):
    """

    :param request:
    :return Solicitud render de URL ,acceso a la vista Blog :

    """
    posts=Post.objects.all()
    return render(request, 'blog/blog.html', {"posts": posts})

def categoria(request,categoria_id):
    """

    :param request:
    :param categoria_id:
    :return: listado de post correspondientes a la categoria
    seleccionada
    """
    categoria=Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(request,'blog/categorias.html', {'categoria':categoria,"posts": posts})