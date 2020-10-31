from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects
import socket
import requests

# Create your views here.
def projects(request):
    hostname = socket.gethostname()
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    allPosts= Projects.objects.all()
    context = {'allPosts': allPosts, 'ip': ip,'device':hostname}
    return render(request, "proj/projhome.html", context)