from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def index(request):
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
    navbar = Navbar.objects.all()
    navbarrighmedia = Navbarrighmedia.objects.all()
    navbarrightcontact = Navbarrightcontact.objects.first()
    footer = Footer.objects.all()
    aboutsheet = Aboutsheet.objects.all()

    context= {
        'navbar': navbar,
        'navbarrightcontact': navbarrightcontact,
        'navbarrighmedia' : navbarrighmedia,
        'footer' : footer,
        'aboutsheet' : aboutsheet
    }


    return render(request, 'about.html', context)

def blog(request):
    navbar = Navbar.objects.all()
    navbarrighmedia = Navbarrighmedia.objects.all()
    navbarrightcontact = Navbarrightcontact.objects.first()
    footer = Footer.objects.all()

    context= {
        'navbar': navbar,
        'navbarrightcontact': navbarrightcontact,
        'navbarrighmedia' : navbarrighmedia,
        'footer' : footer
    }
    return render(request, 'blog.html', context)

def blog_detail(request):
    navbar = Navbar.objects.all()
    navbarrighmedia = Navbarrighmedia.objects.all()
    navbarrightcontact = Navbarrightcontact.objects.first()
    footer = Footer.objects.all()

    context= {
        'navbar': navbar,
        'navbarrightcontact': navbarrightcontact,
        'navbarrighmedia' : navbarrighmedia,
        'footer' : footer
    }
    return render(request, 'blog-detail.html', context)
    
def project(request):
    navbar = Navbar.objects.all()
    navbarrighmedia = Navbarrighmedia.objects.all()
    navbarrightcontact = Navbarrightcontact.objects.first()
    footer = Footer.objects.all()
    projectssheet = Projectssheet.objects.all()

    context= {
        'navbar': navbar,
        'navbarrightcontact': navbarrightcontact,
        'navbarrighmedia' : navbarrighmedia,
        'footer' : footer,
        'projectssheet' : projectssheet
    }
    return render(request, 'projects.html', context)