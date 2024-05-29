from django.contrib import admin

from seminar.models import Seminar_turlari, Seminar, Seminar_majlislari


@admin.register(Seminar_turlari)
class Seminar_turlariAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_ru', 'title_en', 'status', 'order',]


@admin.register(Seminar)
class SeminarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_ru', 'title_en', 'subcontent_uz', 'subcontent_en', 'subcontent_ru', 'seminar_id',
              'status', 'order',]


@admin.register(Seminar_majlislari)
class Seminar_majlislariAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_ru', 'title_en', 'content_en', 'content_uz', 'content_ru', 'subcontent_uz',
              'subcontent_en', 'subcontent_ru', 'file', 'data', 'seminar_id', 'status', 'order',]


