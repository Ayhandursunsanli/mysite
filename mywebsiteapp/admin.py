from django.contrib import admin

# Register your models here.

from .models import *
from django.contrib.auth.models import User
from modeltranslation.admin import TranslationAdmin

# admin.site.register(Deneme)


#Navbar Title tr-en
@admin.register(Navbar)
class NavbarAdmin(TranslationAdmin):
    list_display = ("title",)

    group_fieldsets = True
    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



admin.site.register(Navbarrightcontact)
admin.site.register(Navbarrighmedia)


#Header carousel tr-en 
@admin.register(Headercarousel)
class HeadercarouselAdmin(TranslationAdmin):
    list_display = ("title", "about")

    group_fieldsets = True
    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



# -------------------------------------------------------------

# class FirstSubSectionInline(admin.StackedInline):  
#     model = FirstSubSection

# class SecondSubSectionInline(admin.StackedInline):  
#     model = SecondSubSection

# @admin.register(Indexsectionone)
# class IndexSectionOneAdmin(admin.ModelAdmin):
#     list_display = ('title',)
#     inlines = [FirstSubSectionInline, SecondSubSectionInline]

class FirstSubSectionInline(admin.StackedInline):
    model = FirstSubSection
    max_num = 1  # Yalnızca bir örnek olacak

class SecondSubSectionInline(admin.StackedInline):
    model = SecondSubSection
    max_num = 1  # Yalnızca bir örnek olacak

@admin.register(Indexsectionone)
class IndexSectionOneAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [FirstSubSectionInline, SecondSubSectionInline]


class FirstSubSectionThreeInline(admin.StackedInline):
    model = FirstSubSectionThree
    # max_num = 1  # Yalnızca bir örnek olacak

@admin.register(Indexsectionthree)
class IndexSectionThreeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [FirstSubSectionThreeInline]


class FirstSubSectionFourInline(admin.StackedInline):
    model = FirstSubSectionFour
    max_num = 1  # Yalnızca bir örnek olacak

@admin.register(Indexsectionfour)
class IndexSectionFourAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [FirstSubSectionFourInline]




class FirstSubSectionFiveInline(admin.StackedInline):
    model = FirstSubSectionFive
    # max_num = 1  # Yalnızca bir örnek olacak

@admin.register(Indexsectionfive)
class IndexSectionFiveAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [FirstSubSectionFiveInline]



admin.site.register(Indexsectionsix)




class FooterSubSectionInline(admin.StackedInline):
    model = FooterSubSection
    # max_num = 1  # Yalnızca bir örnek olacak

class FooterSupSectionInline(admin.StackedInline):
    model = FooterSupSection

@admin.register(Footer)
class FooterSubSectionAdmin(admin.ModelAdmin):
    list_display = ('description',)
    inlines = [FooterSubSectionInline, FooterSupSectionInline]


# Projects.html

class ProjectCardInline(admin.StackedInline):
    model = ProjectCard


@admin.register(Projectssheet)
class ProjectssheetAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ProjectCardInline,]


# About.html
# class CertificateInline(admin.StackedInline):
#     model = Certificate
#     max_num = 1  # Yalnızca bir örnek olacak

# class MyskillsInline(admin.StackedInline):
#     model = Myskills
#     max_num = 1  # Yalnızca bir örnek olacak

# admin.register(Aboutsheet)
# class AboutsheetAdmin(admin.ModelAdmin):
#     list_display = ('title',)
#     inlines = [CertificateInline, MyskillsInline]


class CertificateInline(admin.StackedInline):
    model = Certificate
    max_num = 1

class MyskillsInline(admin.StackedInline):
    model = Myskills
    max_num = 1

class AboutsheetAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [CertificateInline, MyskillsInline]

admin.site.register(Aboutsheet, AboutsheetAdmin)




# blog
admin.site.register(Blog)