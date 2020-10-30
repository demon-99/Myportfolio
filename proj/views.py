from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects

# Create your views here.
def projects(request):
    allPosts= Projects.objects.all()
    context={'allPosts': allPosts}
    return render(request, "proj/projhome.html", context)