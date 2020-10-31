from django.shortcuts import render, HttpResponse
from .models import Post
import socket
import requests

# Create your views here.
def blogHome(request):
    hostname = socket.gethostname()
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    allPosts= Post.objects.all()
    context = {'allPosts': allPosts, 'ip': ip,'device':hostname}
    return render(request, "blog/bloghome.html", context)

def blogPost(request, slug):
    hostname = socket.gethostname()
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post, 'ip': ip,'device':hostname}
    return render(request, 'blog/blogpost.html', context)