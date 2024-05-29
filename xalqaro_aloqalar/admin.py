from django.contrib import admin

from xalqaro_aloqalar.models import Xamkor_tashkilot, Xamkor_loihalar, Xalqaro_tadqiqot, Xalqaro_sayohatlar


@admin.register(Xamkor_tashkilot)
class Xamkor_tashkilotAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'subcontent_uz',
                       'subcontent_ru', 'subcontent_en', 'file', 'status', 'order',]


@admin.register(Xamkor_loihalar)
class Xamkor_loihalarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'subcontent_uz',
                       'subcontent_ru', 'subcontent_en', 'file', 'status', 'order', ]


@admin.register(Xalqaro_tadqiqot)
class Xalqaro_tadqiqotAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'subcontent_uz',
                       'subcontent_ru', 'subcontent_en', 'file', 'status', 'order', ]


@admin.register(Xalqaro_sayohatlar)
class Xalqaro_sayohatlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'subcontent_uz',
                       'subcontent_ru', 'subcontent_en', 'file', 'status', 'order', ]
