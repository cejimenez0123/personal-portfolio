from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def home(request):
    projects = Project.objects.order_by('title')
    return render(request, 'portfolio/home.html', {'projects' : projects})