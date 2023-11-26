from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def index(request):
    # deneme = Deneme.objects.all()

    # context = { 
    #     'deneme': deneme
    # }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def blog_detail(request):
    return render(request, 'blog-detail.html')
    
def project(request):
    return render(request, 'projects.html')