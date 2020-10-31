from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects
import socket

# Create your views here.
def projects(request):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    allPosts= Projects.objects.all()
    context = {'allPosts': allPosts, 'ip': ip_address,'device':hostname}
    return render(request, "proj/projhome.html", context)