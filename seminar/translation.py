from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import *


@register(Seminar_turlari)
class Seminar_turlariTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Seminar)
class SeminarTranslationOptions(TranslationOptions):
    fields = ('title', 'subcontent')


@register(Seminar_majlislari)
class Seminar_majlislariTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'subcontent')


