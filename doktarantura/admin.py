from django.contrib import admin
from .models import Qabul_tartibi, Malakaviy_imtihon, Doktarantura


@admin.register(Qabul_tartibi)
class Qabul_tartibiAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'file', 'status', 'order',]


@admin.register(Malakaviy_imtihon)
class Malakaviy_imtihonAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'file', 'status', 'order',]


@admin.register(Doktarantura)
class DoktaranturaAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'file', 'type', 'status',
              'order',]
