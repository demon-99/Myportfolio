from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects
import socket
import requests

# Create your views here.
def projects(request):
    hostname = socket.gethostname()
    ip_address = requests.get('https://api.ipify.org').text
    allPosts= Projects.objects.all()
    context = {'allPosts': allPosts, 'ip': ip_address,'device':hostname}
    return render(request, "proj/projhome.html", context)