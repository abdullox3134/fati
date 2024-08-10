from modeltranslation.translator import TranslationOptions
# from .models import Institut_ken_azolari, Ilmiy_kengash_majlis, Qabul_korib_gan_dissertatsiya, Shifr_va_passport, \
# Dissertatsiya_va_avtoref, Dissertatsiya_fayllar, Yosh_olimlar, Yosh_olimlar_azolari, Maruzalar
from modeltranslation.decorators import register
from .models import Ilmiy_kengash_majlis, Institut_ken_azolari, Yosh_olimlar


@register(Institut_ken_azolari)
class Institut_ken_azolariTranslationOptions(TranslationOptions):
    fields = ('title', )
#


@register(Ilmiy_kengash_majlis)
class Ilmiy_kengash_majlisTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'subcontent',)

#
# @register(Qabul_korib_gan_dissertatsiya)
# class Qabul_korib_gan_dissertatsiyaTranslationOptions(TranslationOptions):
#     fields = ('title', 'content', )
#
#
# @register(Shifr_va_passport)
# class Shifr_va_passportTranslationOptions(TranslationOptions):
#     fields = ('title', )
#
#
# @register(Dissertatsiya_va_avtoref)
# class Dissertatsiya_va_avtorefTranslationOptions(TranslationOptions):
#     fields = ('title', 'content', )
#
#
# @register(Dissertatsiya_fayllar)
# class Dissertatsiya_fayllarTranslationOptions(TranslationOptions):
#     fields = ('title', 'content', )
#
#
@register(Yosh_olimlar)
class Yosh_olimlarTranslationOptions(TranslationOptions):
    fields = ('title', 'content', )

#
# @register(Yosh_olimlar_azolari)
# class Yosh_olimlar_azolariTranslationOptions(TranslationOptions):
#     fields = ('title', 'position', 'degree',)


# @register(Maruzalar)
# class MaruzalarTranslationOptions(TranslationOptions):
#     fields = ('title', 'content', 'subcontent', )
#
#
from .models import DissertatsiyaIshlar, Azolar, Content


@register(Azolar)
class DissertatsiyaIshlarTranslationOptions(TranslationOptions):
    fields = ('name', 'ish_joy', 'lavozim', 'ilmiy_darajasi', 'ilmiy_unvoni')


@register(DissertatsiyaIshlar)
class AzolarTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Content)
class contentTranslationOptions(TranslationOptions):
    fields = ('content',)
