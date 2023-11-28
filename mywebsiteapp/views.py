from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def index(request):
    # deneme = Deneme.objects.all()

    # context = { 
    #     'deneme': deneme
    # }

    navbar = Navbar.objects.all()
    navbarrighmedia = Navbarrighmedia.objects.all()
    navbarrightcontact = Navbarrightcontact.objects.first()
    headercarousel = Headercarousel.objects.all()
    index_section_one_data = Indexsectionone.objects.all()
    index_section_three_data = Indexsectionthree.objects.all()
    index_section_four_data = Indexsectionfour.objects.all()
    index_section_five_data = Indexsectionfive.objects.all()
    index_section_six_data = Indexsectionsix.objects.all()
    footer = Footer.objects.all()

    context= {
        'navbar': navbar,
        'navbarrightcontact': navbarrightcontact,
        'navbarrighmedia' : navbarrighmedia,
        'headercarousel': headercarousel,
        'index_section_one_data': index_section_one_data,
        'index_section_three_data': index_section_three_data,
        'index_section_four_data': index_section_four_data,
        'index_section_five_data': index_section_five_data,
        'index_section_six_data': index_section_six_data,
        'footer' : footer
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def blog_detail(request):
    return render(request, 'blog-detail.html')
    
def project(request):
    return render(request, 'projects.html')