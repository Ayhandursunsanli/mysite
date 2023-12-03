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





class Indexsectionfour(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Anasayfa - Section-4"
        verbose_name_plural = "Anasayfa Section-4"

class FirstSubSectionFour(models.Model):
    section = models.ForeignKey(Indexsectionfour, on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=250)
    description = RichTextField()
    sue = RichTextField()
    analysis = RichTextField()
    design = RichTextField()
    coding = RichTextField()
    testing_release = RichTextField()
    maintenance_support = RichTextField()





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
    

class Indexsectionsix(models.Model):
    description = RichTextField()

    class Meta:
        verbose_name = "Anasayfa - Section-6 (Seo Alanı)"
        verbose_name_plural = "Anasayfa - Section-6 (Seo Alanı)"





class Footer(models.Model):
    description = RichTextField()
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


# projects.html

class Projectssheet(models.Model):
    title = models.CharField(max_length=250)
    about = RichTextField()

    class Meta:
        verbose_name = "Projelerim Sayfası"
        verbose_name_plural = "Projelerim Sayfası"

class ProjectCard(models.Model):
    section = models.ForeignKey(Projectssheet, on_delete=models.CASCADE)
    site_title = models.CharField(max_length=500)
    site_img = models.ImageField(upload_to='Projectscard_images/')
    site_img_logo = models.ImageField(upload_to='Projectscard_images/')
    site_url = models.URLField()




# about.html
class Aboutsheet(models.Model):
    title = models.CharField(max_length=250)
    about = RichTextField()
    img = models.ImageField(upload_to='about_images/' , null=True)

    class Meta:
        verbose_name = "Hakkımda Sayfası"
        verbose_name_plural = "Hakkımda Sayfası"

class Certificate(models.Model):
    section = models.ForeignKey(Aboutsheet, on_delete=models.CASCADE)
    cert_title = models.CharField(max_length=500)
    cert_about = RichTextField()
    cert_img1 = models.ImageField(upload_to='Certificate_images/', null=True, blank=True)
    cert_img2 = models.ImageField(upload_to='Certificate_images/', null=True, blank=True)
    cert_img3 = models.ImageField(upload_to='Certificate_images/', null=True, blank=True)
    cert_img4 = models.ImageField(upload_to='Certificate_images/', null=True, blank=True)
    cert_img5 = models.ImageField(upload_to='Certificate_images/', null=True, blank=True)

class Myskills(models.Model):
    section = models.ForeignKey(Aboutsheet, on_delete=models.CASCADE)
    skill_title = models.CharField(max_length=500)
    skill_about = RichTextField()
    skill_img1 = models.ImageField(upload_to='Skill_images/', null=True, blank=True)
    skill_img2 = models.ImageField(upload_to='Skill_images/', null=True, blank=True)
    skill_img3 = models.ImageField(upload_to='Skill_images/', null=True, blank=True)
    skill_img4 = models.ImageField(upload_to='Skill_images/', null=True, blank=True)
    skill_img4 = models.ImageField(upload_to='Skill_images/', null=True, blank=True)
    skill_img5 = models.ImageField(upload_to='Skill_images/', null=True, blank=True)
    skill_img6 = models.ImageField(upload_to='Skill_images/', null=True, blank=True)
    skill_img7 = models.ImageField(upload_to='Skill_images/', null=True, blank=True)
    skill_img8 = models.ImageField(upload_to='Skill_images/', null=True, blank=True)
    skill_img9 = models.ImageField(upload_to='Skill_images/', null=True, blank=True)
    skill_img10 = models.ImageField(upload_to='Skill_images/', null=True, blank=True)


# blog
class Blog(models.Model):
    image = models.ImageField(upload_to='blog_images/')
    title = models.CharField(max_length=250)
    text = RichTextField()
    subject = models.CharField(max_length=250)
    subject_icon = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title