from django.shortcuts import render
from blog.models import Post

# Create your views here.
# <img class="intro-img img-fluid mb-3 mb-lg-0 rounded" src="{{post.imagen.url}}" alt="" style="width: 50%;">
def blog(request):
    """

    :param request:
    :return Solicitud render de URL ,acceso a la vista Blog :

    """
    posts=Post.objects.all()
    return render(request, 'blog/blog.html', {"posts": posts})