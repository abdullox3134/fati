from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import *


@register(Institut_tarixi)
class Institut_tarixiTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'subcontent')


@register(Memory_hujjatlar)
class Memory_hujjatlarTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Elonlar)
class ElonlarTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Karusel)
class KaruselTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Rahbariyat)
class RahbariyatTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Tashkiliy_tuzulma)
class Tashkiliy_tuzulmaTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Yangiliklar)
class YangiliklarTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'subcontent',)


@register(Havolalar)
class HavolalarTranslationOptions(TranslationOptions):
    fields = ('title',)


