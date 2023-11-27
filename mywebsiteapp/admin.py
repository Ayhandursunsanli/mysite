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










