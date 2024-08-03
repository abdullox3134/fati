from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import Qabul_tartibi, Malakaviy_imtihon, Doktarantura


@register(Qabul_tartibi)
class Qabul_tartibiTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Malakaviy_imtihon)
class Malakaviy_imtihonTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Doktarantura)
class DoktaranturaTranslationOptions(TranslationOptions):
    fields = ('title', 'mehnat_faolyati', 'ilimiy_faolyati', 'asarlar')
