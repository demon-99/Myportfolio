from django.shortcuts import render
from django.http import HttpResponse
from proj.models import Projects

# Create your views here.
def index(request):
    return render(request,'home/home.html')

def about(request):
    allPosts = Projects.objects.all()
    context = {'allPosts': allPosts}
    return render(request,'home/about.html', context)