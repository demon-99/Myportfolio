from django.shortcuts import render
from django.http import HttpResponse
from proj.models import Projects
import socket

# Create your views here.
def index(request):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    context = {'ip': ip_address, 'device': hostname}
    return render(request,'home/home.html', context)

def about(request):
    allPosts = Projects.objects.all()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    context = {'allPosts': allPosts, 'ip': ip_address,'device':hostname}
    return render(request,'home/about.html', context)