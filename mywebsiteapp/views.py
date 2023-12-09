from django.shortcuts import render, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .forms import ContactForm
from django.shortcuts import redirect
import time
from .models import *
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

# Create your views here.

def get_common_context():
    navbar = Navbar.objects.all()
    navbarrighmedia = Navbarrighmedia.objects.all()
    navbarrightcontact = Navbarrightcontact.objects.first()
    footer = Footer.objects.all()
    
    common_context = {
        'navbar': navbar,
        'navbarrightcontact': navbarrightcontact,
        'navbarrighmedia' : navbarrighmedia,
        'footer' : footer,
    }
    
    return common_context

def index(request):
    common_context = get_common_context()
    headercarousel = Headercarousel.objects.all()
    index_section_one_data = Indexsectionone.objects.all()
    index_section_three_data = Indexsectionthree.objects.all()
    index_section_four_data = Indexsectionfour.objects.all()
    index_section_five_data = Indexsectionfive.objects.all()
    index_section_six_data = Indexsectionsix.objects.all()
    indexpagemap = Indexpagemap.objects.all()

    common_context['headercarousel'] = headercarousel
    common_context['index_section_one_data'] =  index_section_one_data
    common_context['index_section_three_data'] = index_section_three_data
    common_context['index_section_four_data'] = index_section_four_data
    common_context['index_section_five_data'] = index_section_five_data
    common_context['index_section_six_data'] = index_section_six_data
    common_context['indexpagemap'] = indexpagemap


    return render(request, 'index.html', common_context)

def about(request):
    common_context = get_common_context()
    aboutsheet = Aboutsheet.objects.all()

    common_context['aboutsheet'] = aboutsheet

    return render(request, 'about.html', common_context)

def blog(request):
    common_context = get_common_context()
    blogList = Bloglist.objects.first()
    blogs = BlogWrite.objects.all().order_by('-publish_date')

    common_context['blogList'] = blogList
    common_context['blogs'] = blogs

    return render(request, 'blog.html', common_context)

def blog_detail(request, blog_id):
    common_context = get_common_context()
    blog = get_object_or_404(BlogWrite, pk=blog_id)
    blogDetail_sheet = Blog.objects.first()

    common_context['blog'] = blog
    common_context['blogDetail_sheet'] = blogDetail_sheet

    return render(request, 'blog-detail.html', common_context)
    
def project(request):
    common_context = get_common_context()
    projectssheet = Projectssheet.objects.all()

    common_context['projectssheet'] = projectssheet

    return render(request, 'projects.html', common_context)

def contact_us(request):
    navbar = Navbar.objects.all()
    navbarrighmedia = Navbarrighmedia.objects.all()
    navbarrightcontact = Navbarrightcontact.objects.first()
    footer = Footer.objects.all()
    contactsheet = Contactsheet.objects.first()

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
            thankyou = Thankyou.objects.first()

            context = {
                'thankyou' : thankyou,
            }
            # İşlem başarılıysa teşekkür sayfasına yönlendirme
            return render(request, 'thank_you.html', context)
            
    else:
        form = ContactForm()

    context = {
        'navbar': navbar,
        'navbarrightcontact': navbarrightcontact,
        'navbarrighmedia': navbarrighmedia,
        'footer': footer,
        'form': form,
        'contactsheet': contactsheet,  
    }
    return render(request, 'contact-us.html', context)

def teams(request):
    common_context = get_common_context()

    return render(request, 'teams.html', common_context)


def thank_you(request):
    return render(request, 'thank_you.html')

def loading_page(request):
    return render(request, 'includes/_loading.html')

def set_language(request, language):
    print(f"Language parameter received: {language}")
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response