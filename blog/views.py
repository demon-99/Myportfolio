from django.shortcuts import render, HttpResponse
from .models import Post
import socket
import requests

# Create your views here.
def blogHome(request):
    hostname = socket.gethostname()
    ip_address = requests.get('https://api.ipify.org').text
    allPosts= Post.objects.all()
    context = {'allPosts': allPosts, 'ip': ip_address,'device':hostname}
    return render(request, "blog/bloghome.html", context)

def blogPost(request, slug):
    hostname = socket.gethostname()
    ip_address = requests.get('https://api.ipify.org').text
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post, 'ip': ip_address,'device':hostname}
    return render(request, 'blog/blogpost.html', context)