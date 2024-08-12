from django.contrib import admin
# from kutobxona.models import Category, Archive, DissertationsAndAbstracts, Editor, Requirements
from .models import Talablar
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
#     search_fields = ('title',)
#     fields = ('title_uz', 'title_en', 'status', 'order',)
#
#
# @admin.register(Archive)
# class ArchiveAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
#     search_fields = ('title',)
#     fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'sub_content_uz',
#               'sub_content_en', 'file', 'base_file', 'status', 'order',)
#
#
# @admin.register(DissertationsAndAbstracts)
# class DissertationsAndAbstractsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'status', 'created_at', 'updated_at', 'order',)
#     search_fields = ('title',)
#     fields = ('title_uz', 'title_en', 'category', 'content_uz', 'content_en',
#               'image', 'file', 'status', 'order',)
#
#
# @admin.register(Editor)
# class EditorAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'email', 'created_at', 'updated_at', 'order')
#     search_fields = ('title')
#     fields = ('title_uz', 'title_en', 'position_uz', 'position_en', 'degree_uz', 'degree_en', 'sphere_uz', 'sphere_en',
#               'content_uz', 'content_en', 'email', 'file', 'status', 'order',)
from django.contrib import admin
from .models import Maqola, Tahrirchi, ArxivSon, Avtoreferat, Manba, ElektronKitob
from django.contrib import admin
from .models import ArxivMenu, Arxiv


@admin.register(Talablar)
class RequirementsAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'Updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'sub_content_uz',
              'sub_content_en', 'file', 'status', 'order',)


class TahrirchiAdmin(admin.ModelAdmin):
    list_display = ('title',  'created_at', 'Updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'ish_joyi', 'lavozimi', 'status', 'order',]


class ArxivSonAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'Updated_at', 'order',)
    search_fields = ('content',)
    fields = ['content_uz', 'content_en', 'file_url', 'status', 'order',]


class MaqolaAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'Updated_at', 'order',)
    search_fields = ('content',)
    fields = ('content_uz', 'content_en', 'tahrirchilar', 'arxiv_sonlar', 'status', 'order',)


@admin.register(Avtoreferat)
class AvtoreferatAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'Updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'cover_img', 'file', 'status', 'order',]


@admin.register(ElektronKitob)
class ElektronKitobAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'Updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'cover_img', 'file', 'status', 'order',]


@admin.register(Manba)
class ManbaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'Updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'cover_img', 'file', 'status', 'order',]


@admin.register(Arxiv)
class ArxivAdmin(admin.ModelAdmin):
    list_display = ('yil', 'nashr_raqami', 'status', 'order', 'created_at', 'Updated_at',)
    search_fields = ('yil', 'nashr_raqami')
    fields = ['yil', 'nashr_raqami', 'file_url', 'arxiv_list', 'status', 'order',]


@admin.register(ArxivMenu)
class ArxivMenuAdmin(admin.ModelAdmin):
    list_display = ('davr_oraligi', 'content', 'status', 'order', 'created_at', 'Updated_at')
    search_fields = ('davr_oraligi',)
    fields = ['davr_oraligi', 'content_uz', 'content_en', 'status', 'order',]


# admin.site.register(Arxiv, ArxivAdmin)
# admin.site.register(ArxivMenu, ArxivMenuAdmin)


admin.site.register(Tahrirchi, TahrirchiAdmin)
admin.site.register(ArxivSon, ArxivSonAdmin)
admin.site.register(Maqola, MaqolaAdmin)
# admin.site.register(Avtoreferat, AvtoreferatAdmin)
# admin.site.register(Manba, ManbaAdmin)
# admin.site.register(ElektronKitob, ElektronKitobAdmin)