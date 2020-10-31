from django.shortcuts import render
from django.http import HttpResponse
from proj.models import Projects
import socket
import requests

# Create your views here.
def index(request):
    hostname = socket.gethostname()
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    context = {'ip': ip, 'device': hostname}
    return render(request,'home/home.html', context)

def about(request):
    allPosts = Projects.objects.all()
    hostname = requests.get('https://api.ipify.org').text
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    context = {'allPosts': allPosts, 'ip': ip,'device':hostname}
    return render(request,'home/about.html', context)