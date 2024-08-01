from django.contrib import admin

from qoshimcha_malumotlar.models import Institut_tarixi, Aloqa, Karusel, Rahbariyat, \
    Tashkiliy_tuzulma, Yangiliklar, Havolalar


@admin.register(Institut_tarixi)
class Institut_tarixiAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en',
              'subcontent_uz', 'subcontent_ru', 'subcontent_en', 'file', 'base_file', 'status', 'order',]


# @admin.register(Memory_hujjatlar)
# class Memory_hujjatlarAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
#     search_fields = ('title',)
#     fields = ['title_uz', 'title_ru', 'title_en', 'file', 'status', 'order',]
#
#
# @admin.register(Elonlar)
# class ElonlarAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'type', 'order',)
#     search_fields = ('title',)
#     fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'file', 'type', 'status',
#               'order',]


@admin.register(Aloqa)
class AloqaAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Karusel)
class KaruselAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'file',
              'link', 'status', 'order']


@admin.register(Rahbariyat)
class RahbariyatAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_ru', 'title_en', 'position', 'degree', 'contact', 'days', 'image', 'status', 'order',]


@admin.register(Tashkiliy_tuzulma)
class Tashkiliy_tuzulmaAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'file', 'order', 'status',]


@admin.register(Yangiliklar)
class YangiliklarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru',
              'content_en', 'subcontent_uz', 'subcontent_en', 'subcontent_ru', 'file', 'status', 'order']


@admin.register(Havolalar)
class HavolalarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_ru', 'title_en', 'file', 'link', 'status', 'order',]