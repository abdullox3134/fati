from django.contrib import admin

from kengashlar.models import Institut_ken_azolari, Ilmiy_kengash_majlis, Qabul_korib_gan_dissertatsiya, \
    Shifr_va_passport, Dissertatsiya_va_avtoref, Dissertatsiya_fayllar, Yosh_olimlar, Yosh_olimlar_azolari, Maruzalar


@admin.register(Institut_ken_azolari)
class Institut_ken_azolariAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'title_en', 'file', 'status', 'order',)


@admin.register(Ilmiy_kengash_majlis)
class Ilmiy_kengash_majlisAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'subcontent_uz',
              'subcontent_ru', 'subcontent_en', 'file', 'date', 'status', 'order',)


@admin.register(Qabul_korib_gan_dissertatsiya)
class Qabul_korib_gan_dissertatsiyaAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'file', 'status', 'order',)


@admin.register(Shifr_va_passport)
class Shifr_va_passportAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'title_en', 'file', 'date', 'status', 'order',)


@admin.register(Dissertatsiya_va_avtoref)
class Dissertatsiya_va_avtorefAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'status', 'order',)


@admin.register(Dissertatsiya_fayllar)
class Dissertatsiya_fayllarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'file', 'base_file',
              'status', 'order',)


@admin.register(Yosh_olimlar)
class Yosh_olimlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'file', 'status', 'order',)


@admin.register(Yosh_olimlar_azolari)
class Yosh_olimlar_azolariAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'title_en', 'position_uz', 'position_ru', 'position_en', 'degree_uz', 'degree_ru',
              'degree_en', 'contact_uz', 'contact_ru', 'contact_en', 'email', 'file', 'status', 'order',)


@admin.register(Maruzalar)
class MaruzalarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'subcontent_uz',
              'subcontent_ru', 'subcontent_en', 'file', 'data', 'status', 'order',)
