from django.shortcuts import render, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .forms import ContactForm
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
    blogs = Blog.objects.all()

    context= {
        'navbar': navbar,
        'navbarrightcontact': navbarrightcontact,
        'navbarrighmedia' : navbarrighmedia,
        'footer' : footer,
        'blogs': blogs
    }
    return render(request, 'blog.html', context)

def blog_detail(request, blog_id):
    navbar = Navbar.objects.all()
    navbarrighmedia = Navbarrighmedia.objects.all()
    navbarrightcontact = Navbarrightcontact.objects.first()
    footer = Footer.objects.all()
    blog = get_object_or_404(Blog, pk=blog_id)

    context= {
        'navbar': navbar,
        'navbarrightcontact': navbarrightcontact,
        'navbarrighmedia' : navbarrighmedia,
        'footer' : footer,
        'blog': blog
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


# def contact_us(request):
#     navbar = Navbar.objects.all()
#     navbarrighmedia = Navbarrighmedia.objects.all()
#     navbarrightcontact = Navbarrightcontact.objects.first()
#     footer = Footer.objects.all()

#     context= {
#         'navbar': navbar,
#         'navbarrightcontact': navbarrightcontact,
#         'navbarrighmedia' : navbarrighmedia,
#         'footer' : footer
#     }
#     return render(request, 'contact-us.html', context)

def contact_us(request):
    navbar = Navbar.objects.all()
    navbarrighmedia = Navbarrighmedia.objects.all()
    navbarrightcontact = Navbarrightcontact.objects.first()
    footer = Footer.objects.all()

    # İletişim formunu oluşturun
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Mesajı işleyip e-posta olarak gönderme
            send_mail(
                subject,
                f"Name: {name}\nEmail: {email}\n\n{message}",
                email,
                ['ayhandursunsanli@gmail.com'],  # Buraya kendi e-posta adresinizi ekleyin
                fail_silently=False,
            )

            # İşlem başarılıysa teşekkür sayfasına yönlendirme
            return render(request, 'thank_you.html')
    else:
        form = ContactForm()

    context = {
        'navbar': navbar,
        'navbarrightcontact': navbarrightcontact,
        'navbarrighmedia': navbarrighmedia,
        'footer': footer,
        'form': form,  # İletişim formunu context'e ekleyin
    }
    return render(request, 'contact-us.html', context)


# mesaj gönderdikten sonra gidilecek sayfa
def thank_you(request):
    return render(request, 'thank_you.html')

