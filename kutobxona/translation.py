from modeltranslation.translator import TranslationOptions
from .models import Category, DissertationsAndAbstracts, Editor, Archive, Requirements
from modeltranslation.decorators import register


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(DissertationsAndAbstracts)
class DissertationsAndAbstractsTranslationOptions(TranslationOptions):
    fields = ('title', 'content', )


@register(Editor)
class EditorTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'position', 'degree', 'sphere')


@register(Archive)
class ArchiveTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'sub_content',)


@register(Requirements)
class RequirementsTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'sub_content',)

