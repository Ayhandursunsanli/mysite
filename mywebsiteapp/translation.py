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




#*index section four
@register(Indexsectionfour)
class IndexsectionfourTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'description', 'buttonText',)
    
@register(FirstSubSectionFour)
class FirstSubSectionFourTranslationOptions(TranslationOptions):
    fields = ('sueTitle', 'sue', 'analysisTitle', 'analysis', 'designTitle', 'design', 'codingTitle', 'coding', 'testingTitle', 'testing_release', 'maintenance_support_title', 'maintenance_support', )



#*index section five
@register(Indexsectionfive)
class IndexsectionfiveTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'description',)

@register(FirstSubSectionFive)
class FirstSubSectionFiveTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)


#*index section six
@register(Indexsectionsix)
class IndexsectionsixTranslationOptions(TranslationOptions):
    fields = ('description',)


#*Index Page Map
@register(Indexpagemap)
class IndexPageMapTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(IndexPageMapSubSection)
class IndexPageMapSubSectionTranslationOptions(TranslationOptions):
    fields = ('href_title',)



#*footer
@register(Footer)
class FooterTranslationOptions(TranslationOptions):
    fields = ('description', 'titleOne', 'titleTwo', 'titleThree',)

@register(FooterSubSection)
class FooterSubSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'url',)


#*project
@register(Projectssheet)
class ProjectsSheetTranslationOptions(TranslationOptions):
    fields = ('breadcrumbOne', 'breadcrumbTwo', 'headTitle', 'title', 'about',)
@register(ProjectCard)
class ProjectCardTranslationOptions(TranslationOptions):
    fields = ('site_title', 'buttonText',)


#*about
@register(Aboutsheet)
class AboutSheetTranslationOptions(TranslationOptions):
    fields = ('breadcrumbOne', 'breadcrumbTwo', 'headTitle',)
    
@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'about',)

@register(Certificate)
class CertificateTranslationOptions(TranslationOptions):
    fields = ('cert_title', 'cert_about',)

@register(Myskills)
class MySkillsTranslationOptions(TranslationOptions):
    fields = ('skill_title', 'skill_about',)




#*contact
@register(Contactsheet)
class ContactSheetTranslationOptions(TranslationOptions):
    fields = ('breadcrumbOne', 'breadcrumbTwo', 'headTitle', 'subtitle', 'about', 'buttonText',)