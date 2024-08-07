from modeltranslation.translator import TranslationOptions
from .models import Avtoreferat, Manba, Maqola, ArxivSon, Tahrirchi, ElektronKitob
from modeltranslation.decorators import register
#
#
# @register(Category)
# class CategoryTranslationOptions(TranslationOptions):
#     fields = ('title', )
#
#
# @register(DissertationsAndAbstracts)
# class DissertationsAndAbstractsTranslationOptions(TranslationOptions):
#     fields = ('title', 'content', )
#
#
# @register(Editor)
# class EditorTranslationOptions(TranslationOptions):
#     fields = ('title', 'content', 'position', 'degree', 'sphere')
#
#
# @register(Archive)
# class ArchiveTranslationOptions(TranslationOptions):
#     fields = ('title', 'content', 'sub_content',)
#
#
# @register(Requirements)
# class RequirementsTranslationOptions(TranslationOptions):
#     fields = ('title', 'content', 'sub_content',)
#


@register(Avtoreferat)
class AvtoreferatTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Manba)
class ManbaTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Maqola)
class MaqolaTranslationOptions(TranslationOptions):
    fields = ('content',)


@register(ArxivSon)
class ArxivSonTranslationOptions(TranslationOptions):
    fields = ('content',)


@register(Tahrirchi)
class TahrirchiTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ElektronKitob)
class ArxivSonTranslationOptions(TranslationOptions):
    fields = ('title',)