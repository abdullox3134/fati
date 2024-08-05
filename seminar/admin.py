from django.contrib import admin

from seminar.models import Seminar_turlari, Seminar, Seminar_majlislari


@admin.register(Seminar_turlari)
class Seminar_turlariAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'status', 'order',]


@admin.register(Seminar)
class SeminarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'subcontent_uz', 'subcontent_en', 'seminar_id',
              'status', 'order',]


@admin.register(Seminar_majlislari)
class Seminar_majlislariAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_en', 'content_uz', 'subcontent_uz',
              'subcontent_en', 'file', 'data', 'seminar_id', 'status', 'order',]


