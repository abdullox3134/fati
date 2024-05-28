from django.contrib import admin

from seminar.models import Seminar_turlari, Seminar, Seminar_majlislari


@admin.register(Seminar_turlari)
class Seminar_turlariAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Seminar)
class SeminarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Seminar_majlislari)
class Seminar_majlislariAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
