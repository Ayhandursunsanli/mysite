from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

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
    
class Headercarousel(models.Model):
    title = models.CharField(max_length=100)
    about = models.CharField(max_length=500)
    image = models.ImageField(upload_to='headercarousel')

    class Meta:
        verbose_name = "Anasayfa Carousel"
        verbose_name_plural = "Anasayfa Carousel"
    
    
    def __str__(self):
        return self.title
    

class Indexsectionone(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Anasayfa - Section-1"
        verbose_name_plural = "Anasayfa Section-1"

class FirstSubSection(models.Model):
    section = models.ForeignKey(Indexsectionone, on_delete=models.CASCADE)
    carousel_image_1 = models.ImageField(upload_to='indexsectiononecarousel_images/', null=True)
    carousel_image_2 = models.ImageField(upload_to='indexsectiononecarousel_images/', blank=True, null=True)
    carousel_image_3 = models.ImageField(upload_to='indexsectiononecarousel_images/', blank=True, null=True)
    carousel_image_4 = models.ImageField(upload_to='indexsectiononecarousel_images/', blank=True, null=True)
    sub_title = models.CharField(max_length=250)
    description = RichTextField()

class SecondSubSection(models.Model):
    section = models.ForeignKey(Indexsectionone, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subsection_images/')
    sub_title = models.CharField(max_length=250)
    description = RichTextField()


class Indexsectionthree(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Anasayfa - Section-3"
        verbose_name_plural = "Anasayfa Section-3"

class FirstSubSectionThree(models.Model):
    section = models.ForeignKey(Indexsectionthree, on_delete=models.CASCADE)
    carousel_image = models.ImageField(upload_to='indexsectionthreecarousel_images/', null=True)
    sub_title = models.CharField(max_length=250)
    description = RichTextField()


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