from django.contrib import admin

# Register your models here.

from .models import *
from django.contrib.auth.models import User

# admin.site.register(Deneme)

admin.site.register(Navbar)
admin.site.register(Navbarrightcontact)
admin.site.register(Navbarrighmedia)
admin.site.register(Headercarousel)



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


