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

#*index section one
class FirstSubSectionInline(admin.StackedInline):
    model = FirstSubSection
    max_num = 1

class SecondSubSectionInline(admin.StackedInline):
    model = SecondSubSection
    max_num = 1

@admin.register(Indexsectionone)
class IndexSectionOneAdmin(TranslationAdmin):
    list_display = ('title', )
    inlines = [FirstSubSectionInline, SecondSubSectionInline]




#*index section three
class FirstSubSectionThreeInline(admin.StackedInline):
    model = FirstSubSectionThree
    # max_num = 1

@admin.register(Indexsectionthree)
class IndexSectionThreeAdmin(TranslationAdmin):
    list_display = ('title', )
    inlines = [FirstSubSectionThreeInline]




#*index section four
class FirstSubSectionFourInline(admin.StackedInline):
    model = FirstSubSectionFour
    max_num = 1  # Yalnızca bir örnek olacak

@admin.register(Indexsectionfour)
class IndexSectionFourAdmin(TranslationAdmin):
    list_display = ('title',)
    inlines = [FirstSubSectionFourInline]



#*index section five
class FirstSubSectionFiveInline(admin.StackedInline):
    model = FirstSubSectionFive

@admin.register(Indexsectionfive)
class IndexSectionFiveAdmin(TranslationAdmin):
    list_display = ('title',)
    inlines = [FirstSubSectionFiveInline]



#*index section six
@admin.register(Indexsectionsix)
class IndexSectionSixAdmin(TranslationAdmin):
    list_display = ('description',)


#*Index Page Map
class IndexPageMapSubSectionInline(admin.StackedInline):
    model = IndexPageMapSubSection

@admin.register(Indexpagemap)
class IndexPageMapAdmin(TranslationAdmin):
    list_display = ('title',)
    inlines = [IndexPageMapSubSectionInline]



#*footer
class FooterSubSectionInline(admin.StackedInline):
    model = FooterSubSection
    # max_num = 1  # Yalnızca bir örnek olacak

class FooterSupSectionInline(admin.StackedInline):
    model = FooterSupSection

@admin.register(Footer)
class FooterSubSectionAdmin(TranslationAdmin):
    list_display = ('titleOne', 'titleTwo', 'titleThree',)
    inlines = [FooterSubSectionInline, FooterSupSectionInline]





#* Projects.html

class ProjectCardInline(admin.StackedInline):
    model = ProjectCard


@admin.register(Projectssheet)
class ProjectsSheetAdmin(TranslationAdmin):
    list_display = ('headTitle',)
    inlines = [ProjectCardInline,]

class AboutInline(admin.StackedInline):
    model = About
    max_num = 1



#*about.html
@admin.register(Aboutsheet)
class AboutSheetAdmin(TranslationAdmin):
    list_display = ('headTitle',)
    inlines = [AboutInline,]


#*contact sheet
@admin.register(Contactsheet)
class ContactsheetAdmin(TranslationAdmin):
    list_display = ('headTitle',)



#* blog-list (blog.html)
@admin.register(Bloglist)
class BlogListAdmin(TranslationAdmin):
    list_display = ('headTitle',)


#* blog-detail (blog-detail.html)
class BlogWriteInline(admin.StackedInline):
    model = BlogWrite

@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display = ('headTitle',)
    inlines = [BlogWriteInline]


#* thankyou (thank_you.html)
@admin.register(Thankyou)
class ThankyouAdmin(TranslationAdmin):
    list_display = ('title', 'text',)


#*Teams (teams.html)
class PersonInline(admin.StackedInline):
    model = Person

@admin.register(Teamsheet)
class TeamsheetAdmin(TranslationAdmin):
    list_display = ('headTitle',)
    inlines = [PersonInline]
