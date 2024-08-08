from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

from markazlar_va_bolimlar.models import Xodimlar, MarkazlarBolimlar


# from .models import Markazlar_bolimlar, Bolimlar_tarix, Azolarsub, Rasm, Azolar
#
#
# @register(Markazlar_bolimlar)
# class Markazlar_bolimlarTranslationOptions(TranslationOptions):
#     fields = ('title', 'content',)


# @register(Tadqiqot)
# class TadqiqotTranslationOptions(TranslationOptions):
#     fields = ('title', 'content',)


# @register(Bolimlar_tarix)
# class Bolimlar_tarixiTranslationOptions(TranslationOptions):
#     fields = ('title', 'content',)
#
#
# @register(Azolar)
# class AzolariTranslationOptions(TranslationOptions):
#     fields = ('title', 'content', 'academic_degree', 'position')
#
#
# @register(Azolarsub)
# class AzolariTranslationOptions(TranslationOptions):
#     fields = ('title',)
#
#
# # @register(Video)
# # class VideoTranslationOptions(TranslationOptions):
# #     fields = ('title', 'content',)
#
#
# @register(Rasm)
# class RasmTranslationOptions(TranslationOptions):
#     fields = ('title', 'content',)
#


@register(Xodimlar)
class XodimlarTranslationOptions(TranslationOptions):
    fields = ('name', 'lavozim', 'ilmiy_daraja')


@register(MarkazlarBolimlar)
class MarkazlarBolimlarTranslationOptions(TranslationOptions):
    fields = ('tarix',)