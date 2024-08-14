from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

from xalqaro_aloqalar.models import Xamkor_tashkilot, Xamkor_loihalar, Tadqiqot, Xalqaro_sayohatlar, Kelganlar, \
    xamkor_loyihalar_data


@register(Xamkor_tashkilot)
class Xamkor_tashkilotTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'subcontent',)


@register(Xamkor_loihalar)
class Xamkor_loihalarTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(xamkor_loyihalar_data)
class Xamkor_loihalarTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Tadqiqot)
class Xalqaro_tadqiqotTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Kelganlar)
class Xalqaro_tadqiqotTranslationOptions(TranslationOptions):
    fields = ('ism', 'ish_joy',)


@register(Xalqaro_sayohatlar)
class Xalqaro_sayohatlarTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'subcontent',)
