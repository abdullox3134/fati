from modeltranslation.translator import TranslationOptions
from .models import Qabul_tartibi, Malakaviy_imtihon, Doktarantura
from modeltranslation.decorators import register


@register(Qabul_tartibi)
class Qabul_tartibiTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Malakaviy_imtihon)
class Malakaviy_imtihonTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Doktarantura)
class DoktaranturaTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)