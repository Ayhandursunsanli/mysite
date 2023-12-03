from .models import *
from modeltranslation.translator import TranslationOptions, register

#navbar menu
@register(Navbar)
class NavbarTranslationOptions(TranslationOptions):
    fields = ('title',)



# header carousel
@register(Headercarousel)
class HeadercarouselTranslationOptions(TranslationOptions):
    fields = ('title', 'about',)