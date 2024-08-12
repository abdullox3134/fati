from django.contrib import admin

from xalqaro_aloqalar.models import Xamkor_tashkilot, Xamkor_loihalar, Xalqaro_sayohatlar
from .models import Tadqiqot, Kelganlar


@admin.register(Xamkor_tashkilot)
class Xamkor_tashkilotAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz', 'subcontent_en', 'file', 'status',
              'order',]


@admin.register(Xamkor_loihalar)
class Xamkor_loihalarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz', 'subcontent_en', 'file', 'status',
              'order', ]


# @admin.register(Xalqaro_tadqiqot)
# class Xalqaro_tadqiqotAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
#     search_fields = ('title',)
#     fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz', 'subcontent_en',
#               'file', 'status', 'order', ]
#

@admin.register(Xalqaro_sayohatlar)
class Xalqaro_sayohatlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz', 'subcontent_en', 'file', 'status',
              'order', ]


@admin.register(Tadqiqot)
class TadqiqotAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'img_file', 'status', 'order',]


@admin.register(Kelganlar)
class KelganlarAdmin(admin.ModelAdmin):
    list_display = ('ism', 'status', 'created_at', 'updated_at', 'order',)
    list_filter = ('kelgan_yil',)
    search_fields = ('ism',)
    fields = ['tadqiqot', 'kelgan_yil', 'ism_uz', 'ism_en', 'ish_joy_uz', 'ish_joy_en', 'status', 'order',]
