from .models import *
from modeltranslation.translator import TranslationOptions, register

#*navbar menu
@register(Navbar)
class NavbarTranslationOptions(TranslationOptions):
    fields = ('title',)



#* header carousel
@register(Headercarousel)
class HeadercarouselTranslationOptions(TranslationOptions):
    fields = ('title', 'about',)


#*index section one
@register(Indexsectionone)
class IndexsectiononeTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(FirstSubSection)
class FirstSubSectionTranslationOptions(TranslationOptions):
    fields = ('sub_title', 'description',)

@register(SecondSubSection)
class SecondSubSectionTranslationOptions(TranslationOptions):
    fields = ('sub_title', 'description',)



#*index section three
@register(Indexsectionthree)
class IndexsectionthreeTranslationOptions(TranslationOptions):
    fields = ('title', 'buttonText')

@register(FirstSubSectionThree)
class FirstSubSectionThreeTranslationOptions(TranslationOptions):
    fields = ('sub_title', 'description',)

