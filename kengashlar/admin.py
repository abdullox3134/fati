from django.contrib import admin

from kengashlar.models import Institut_ken_azolari, Ilmiy_kengash_majlis, Qabul_korib_gan_dissertatsiya, \
    Shifr_va_passport, Dissertatsiya_va_avtoref, Dissertatsiya_fayllar, Yosh_olimlar, Yosh_olimlar_azolari, Maruzalar


@admin.register(Institut_ken_azolari)
class Institut_ken_azolariAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Ilmiy_kengash_majlis)
class Ilmiy_kengash_majlisAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Qabul_korib_gan_dissertatsiya)
class Qabul_korib_gan_dissertatsiyaAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Shifr_va_passport)
class Shifr_va_passportAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Dissertatsiya_va_avtoref)
class Dissertatsiya_va_avtorefAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Dissertatsiya_fayllar)
class Dissertatsiya_fayllarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Yosh_olimlar)
class Yosh_olimlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Yosh_olimlar_azolari)
class Yosh_olimlar_azolariAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Maruzalar)
class MaruzalarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)