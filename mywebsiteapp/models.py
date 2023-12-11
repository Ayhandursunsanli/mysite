from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

#*Navbar
class Navbar(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Navbar"
        verbose_name_plural = "Navbar"

    def __str__(self):
        return self.title
    
class Navbarrightcontact(models.Model):
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Navbar Sağ Kontak Alanı (Email-Telefon)"
        verbose_name_plural = "Navbar Sağ Kontak Alanı (Email-Telefon)"

    def __str__(self):
        return self.email
    
class Navbarrighmedia(models.Model):
    platform = models.CharField(max_length=50, verbose_name= 'Medya İcon Uzantısı')
    link = models.URLField()

    class Meta:
        verbose_name = "Navbar Sağ Sosyal Medyalar"
        verbose_name_plural = "Navbar Sağ Sosyal Medyalar"
    
    def __str__(self):
        return self.platform
    
    
#*headercarousel    
class Headercarousel(models.Model):
    title = models.CharField(max_length=100, null=True)
    about = models.CharField(max_length=500, null= True)
    image = models.ImageField(upload_to='headercarousel')

    class Meta:
        verbose_name = "Anasayfa Carousel"
        verbose_name_plural = "Anasayfa Carousel"
    
    
    def __str__(self):
        return self.title
    


#*Indexsectionone
class Indexsectionone(models.Model):
    title = models.CharField(max_length=250, null=True)

    class Meta:
        verbose_name = "Anasayfa - Section-1"
        verbose_name_plural = "Anasayfa Section-1"

class FirstSubSection(models.Model):
    section = models.ForeignKey(Indexsectionone, on_delete=models.CASCADE)
    carousel_image_1 = models.ImageField(upload_to='indexsectiononecarousel_images/', null=True)
    carousel_image_2 = models.ImageField(upload_to='indexsectiononecarousel_images/', blank=True, null=True)
    carousel_image_3 = models.ImageField(upload_to='indexsectiononecarousel_images/', blank=True, null=True)
    carousel_image_4 = models.ImageField(upload_to='indexsectiononecarousel_images/', blank=True, null=True)
    sub_title = models.CharField(max_length=250, null=True)
    description = RichTextField(null=True)

class SecondSubSection(models.Model):
    section = models.ForeignKey(Indexsectionone, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subsection_images/', null=True)
    sub_title = models.CharField(max_length=250, null=True)
    description = RichTextField(null=True)


#*Indexsectionthree
class Indexsectionthree(models.Model):
    title = models.CharField(max_length=250, null=True)
    buttonText = models.CharField(max_length=250, null=True)

    class Meta:
        verbose_name = "Anasayfa - Section-3"
        verbose_name_plural = "Anasayfa Section-3"

class FirstSubSectionThree(models.Model):
    section = models.ForeignKey(Indexsectionthree, on_delete=models.CASCADE)
    carousel_image = models.ImageField(upload_to='indexsectionthreecarousel_images/', null=True)
    sub_title = models.CharField(max_length=250, null=True)
    description = RichTextField(null=True)




#*Indexsectionfour
class Indexsectionfour(models.Model):
    title = models.CharField(max_length=250, null=True)
    sub_title = models.CharField(max_length=250, null=True)
    description = RichTextField(null=True)
    buttonText = models.CharField(max_length=250, null=True)


    class Meta:
        verbose_name = "Anasayfa - Section-4"
        verbose_name_plural = "Anasayfa Section-4"

class FirstSubSectionFour(models.Model):
    section = models.ForeignKey(Indexsectionfour, on_delete=models.CASCADE)
    sueTitle = models.CharField(max_length=250, null=True)
    sue = RichTextField(null=True)
    analysisTitle = models.CharField(max_length=250, null=True)
    analysis = RichTextField(null=True)
    designTitle = models.CharField(max_length=250, null=True)
    design = RichTextField(null=True)
    codingTitle = models.CharField(max_length=250, null=True)
    coding = RichTextField(null=True)
    testingTitle = models.CharField(max_length=250, null=True)
    testing_release = RichTextField(null=True)
    maintenance_support_title = models.CharField(max_length=250, null=True)
    maintenance_support = RichTextField(null=True)




#*Indexsectionfive
class Indexsectionfive(models.Model):
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=250)
    description = RichTextField()
    image = models.ImageField(upload_to='indexsectionfive_images/')

    class Meta:
        verbose_name = "Anasayfa - Section-5"
        verbose_name_plural = "Anasayfa Section-5"

class FirstSubSectionFive(models.Model):
    section = models.ForeignKey(Indexsectionfive, on_delete=models.CASCADE)
    question = RichTextField()
    answer = RichTextField()
    



#*Indexsectionsix
class Indexsectionsix(models.Model):
    description = RichTextField(null=True)

    class Meta:
        verbose_name = "Anasayfa - Section-6 (Seo Alanı)"
        verbose_name_plural = "Anasayfa - Section-6 (Seo Alanı)"




#*IndexPageMap
class Indexpagemap(models.Model):
    title = models.CharField(max_length=250, null=True)

    class Meta:
        verbose_name = "Anasayfa - Sayfa Haritası"
        verbose_name_plural = "Anasayfa - Sayfa Haritası"

class IndexPageMapSubSection(models.Model):
    section = models.ForeignKey(Indexpagemap, on_delete=models.CASCADE)
    href_id = models.CharField(max_length=250, null=True)
    href_title = models.CharField(max_length=250, null=True)



#*Footer
class Footer(models.Model):
    description = RichTextField(null=True)
    titleOne = models.CharField(max_length=250, null=True)
    titleTwo = models.CharField(max_length=250, null=True)
    titleThree = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to='footer_images/', null=True, blank=True)
    adress = models.TextField(max_length=250, null=True)
    email = models.EmailField(max_length=250, null=True)
    phone = models.CharField(max_length=250, null=True)

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footer"

class FooterSubSection(models.Model):
    section = models.ForeignKey(Footer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name= 'Menü İtemi', null=True)
    url = models.CharField(max_length=500, verbose_name= 'Menü İtemi Linki', null=True)

class FooterSupSection(models.Model):
    section = models.ForeignKey(Footer, on_delete=models.CASCADE)
    socialmedia = models.CharField(max_length=50, verbose_name= 'Sosyal Medya İcon Uzantısı (Örn: fa fa-github)', null=True)
    socialmedia_link = models.URLField(verbose_name= 'Sosyal Medya İtemi Linki', null=True)


#* projects.html
class Projectssheet(models.Model):
    breadcrumbOne = models.CharField(max_length=250, null=True)
    breadcrumbOneUrl = models.CharField(max_length=250, null=True)
    breadcrumbTwo = models.CharField(max_length=250, null=True)
    headTitle = models.CharField(max_length=250, null=True)
    title = models.CharField(max_length=250, null=True)
    about = RichTextField(null=True)
    

    class Meta:
        verbose_name = "Projelerim Sayfası"
        verbose_name_plural = "Projelerim Sayfası"

class ProjectCard(models.Model):
    section = models.ForeignKey(Projectssheet, on_delete=models.CASCADE)
    site_title = models.CharField(max_length=500, null=True)
    site_about = RichTextField(null=True)
    site_img = models.ImageField(upload_to='Projectscard_images/', null=True)
    site_img_logo = models.ImageField(upload_to='Projectscard_images/', null=True)
    buttonText = models.CharField(max_length=250, null=True)
    site_url = models.URLField(null=True)




#* about.html
class Aboutsheet(models.Model):
    breadcrumbOne = models.CharField(max_length=250, null=True)
    breadcrumbOneUrl = models.CharField(max_length=250, null=True)
    breadcrumbTwo = models.CharField(max_length=250, null=True)
    headTitle = models.CharField(max_length=250, null=True)

    

    class Meta:
        verbose_name = "Hakkımda Sayfası"
        verbose_name_plural = "Hakkımda Sayfası"
    
class About(models.Model):
    section = models.ForeignKey(Aboutsheet, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=True)
    about = RichTextField(null=True)
    img = models.ImageField(upload_to='about_images/' , null=True)

    class Meta:
        verbose_name = "Hakkımda Sayfası"
        verbose_name_plural = "Hakkımda Sayfası"





#* contact.html
class Contactsheet(models.Model):
    breadcrumbOne = models.CharField(max_length=250, null=True)
    breadcrumbOneUrl = models.CharField(max_length=250, null=True)
    breadcrumbTwo = models.CharField(max_length=250, null=True)
    headTitle = models.CharField(max_length=250, null=True)
    subtitle = models.CharField(max_length=250, null=True)
    about = RichTextField(null=True)
    buttonText = models.CharField(max_length=250, null=True)


    class Meta:
        verbose_name = "İletişim Sayfası"
        verbose_name_plural = "İletişim Sayfası"



#*blog-list (blog.html)
class Bloglist(models.Model):
    breadcrumbOne = models.CharField(max_length=250, null=True)
    breadcrumbOneUrl = models.CharField(max_length=250, null=True)
    breadcrumbTwo = models.CharField(max_length=250, null=True)
    headTitle = models.CharField(max_length=250, null=True)
    subtitle = models.CharField(max_length=250, null=True)
    about = RichTextField(null=True)
    authorsub = models.CharField(max_length=250)
    buttonText_subject_all = models.CharField(max_length=250, null=True)
    buttonText = models.CharField(max_length=250, null=True)


#*blog (blog-detail.html (blogDetail_sheet))
class Blog(models.Model):
    breadcrumbOne = models.CharField(max_length=250, null=True)
    breadcrumbOneUrl = models.CharField(max_length=250, null=True)
    breadcrumbTwo = models.CharField(max_length=250, null=True)
    breadcrumbTwoUrl = models.CharField(max_length=250, null=True)
    breadcrumbThree = models.CharField(max_length=250, null=True)
    headTitle = models.CharField(max_length=250, null=True)
    buttonText = models.CharField(max_length=250, null=True)


class BlogWrite(models.Model):
    section = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/', null=True)
    title = models.CharField(max_length=250, null=True)
    text = RichTextField(null=True)
    subject = models.CharField(max_length=250, null=True)
    subject_icon = models.CharField(max_length=250, null=True)
    author = models.CharField(max_length=100, null=True)
    publish_date = models.DateField(auto_now_add=True)


#*thank you
class Thankyou(models.Model):
    title = models.CharField(max_length=250, null=True)
    text = RichTextField(null=True)
    img = models.ImageField(upload_to='thankyou_images/', null=True)



#* teams
class Teamsheet(models.Model):
    breadcrumbOne = models.CharField(max_length=250, null=True)
    breadcrumbOneUrl = models.CharField(max_length=250, null=True)
    breadcrumbTwo = models.CharField(max_length=250, null=True)
    headTitle = models.CharField(max_length=250, null=True)
    subtitle = models.CharField(max_length=250, null=True)
    about = RichTextField(null=True)

class Person(models.Model):
    section = models.ForeignKey(Teamsheet, on_delete=models.CASCADE)
    personName = models.CharField(max_length=250, null=True)
    personJob = models.CharField(max_length=250, null=True)
    personImg = models.ImageField(upload_to='person_images/', null=True)
    socialmediaIcon1 = models.CharField(max_length=250, null=True)
    socialmediaIcon1_url = models.URLField(null=True)
    socialmediaIcon2 = models.CharField(max_length=250, null=True)
    socialmediaIcon2_url = models.URLField(null=True)
    socialmediaIcon3 = models.CharField(max_length=250, null=True)
    socialmediaIcon3_url = models.URLField(null=True)
    about = RichTextField(null=True)
    cvHead = models.CharField(max_length=250, null=True)
    cvYear = models.CharField(max_length=250, null=True)
    cvJob = models.CharField(max_length=250, null=True)
    cvCompany = models.CharField(max_length=250, null=True)
    cvAbout = RichTextField(null=True)
    cvYear2 = models.CharField(max_length=250, null=True, blank=True)
    cvJob2 = models.CharField(max_length=250, null=True, blank=True)
    cvCompany2 = models.CharField(max_length=250, null=True, blank=True)
    cvAbout2 = RichTextField(null=True, blank=True)
    cvYear3 = models.CharField(max_length=250, null=True, blank=True)
    cvJob3 = models.CharField(max_length=250, null=True, blank=True)
    cvCompany3 = models.CharField(max_length=250, null=True, blank=True)
    cvAbout3 = RichTextField(null=True, blank=True)
    cvYear4 = models.CharField(max_length=250, null=True, blank=True)
    cvJob4 = models.CharField(max_length=250, null=True, blank=True)
    cvCompany4 = models.CharField(max_length=250, null=True, blank=True)
    cvAbout4 = RichTextField(null=True, blank=True)
    cvYear5 = models.CharField(max_length=250, null=True, blank=True)
    cvJob5 = models.CharField(max_length=250, null=True, blank=True)
    cvCompany5 = models.CharField(max_length=250, null=True, blank=True)
    cvAbout5 = RichTextField(null=True, blank=True)
    skillAbout = RichTextField(null=True)
    skillImg1 = models.ImageField(upload_to='skill_images/', null=True, blank=True)
    skillImg2 = models.ImageField(upload_to='skill_images/', null=True, blank=True)
    skillImg3 = models.ImageField(upload_to='skill_images/', null=True, blank=True)
    skillImg4 = models.ImageField(upload_to='skill_images/', null=True, blank=True)
    skillImg5 = models.ImageField(upload_to='skill_images/', null=True, blank=True)
    skillImg6 = models.ImageField(upload_to='skill_images/', null=True, blank=True)
    skillImg7 = models.ImageField(upload_to='skill_images/', null=True, blank=True)
    skillImg8 = models.ImageField(upload_to='skill_images/', null=True, blank=True)
    skillImg9 = models.ImageField(upload_to='skill_images/', null=True, blank=True)
    skillImg10 = models.ImageField(upload_to='skill_images/', null=True, blank=True)
    cerAbout = RichTextField(null=True)
    cerImg1 = models.ImageField(upload_to='Certificate_images/', null=True, blank=True)
    cerImg2 = models.ImageField(upload_to='Certificate_images/', null=True, blank=True)
    cerImg3 = models.ImageField(upload_to='Certificate_images/', null=True, blank=True)
    cerImg4 = models.ImageField(upload_to='Certificate_images/', null=True, blank=True)









