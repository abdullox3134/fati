from django.contrib import admin

from qoshimcha_malumotlar.models import Institut_tarixi, Memory_hujjatlar, Elonlar, Aloqa, Karusel, Rahbariyat, \
    Tashkiliy_tuzulma, Yangiliklar, Havolalar


@admin.register(Institut_tarixi)
class Institut_tarixiAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Memory_hujjatlar)
class Memory_hujjatlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Elonlar)
class ElonlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'type', 'order',)
    search_fields = ('title',)


@admin.register(Aloqa)
class AloqaAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Karusel)
class KaruselAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Rahbariyat)
class RahbariyatAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Tashkiliy_tuzulma)
class Tashkiliy_tuzulmaAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Yangiliklar)
class YangiliklarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Havolalar)
class HavolalarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)