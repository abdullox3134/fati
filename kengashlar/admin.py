from django.contrib import admin
#
# from kengashlar.models import Institut_ken_azolari, Ilmiy_kengash_majlis, Qabul_korib_gan_dissertatsiya, \
#     Shifr_va_passport, Dissertatsiya_va_avtoref, Dissertatsiya_fayllar, Yosh_olimlar, Yosh_olimlar_azolari, Maruzalar



from .models import Institut_ken_azolari, Ilmiy_kengash_majlis, Yosh_olimlar
from django.contrib import admin
from .models import Azolar, DissertatsiyaIshlar, Content


@admin.register(Institut_ken_azolari)
class Institut_ken_azolariAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'file', 'status', 'order',)


@admin.register(Ilmiy_kengash_majlis)
class Ilmiy_kengash_majlisAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz',
              'subcontent_en', 'file', 'date', 'status', 'order',)


# @admin.register(Qabul_korib_gan_dissertatsiya)
# class Qabul_korib_gan_dissertatsiyaAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
#     search_fields = ('title',)
#     fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'order',)
#
#
# @admin.register(Shifr_va_passport)
# class Shifr_va_passportAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
#     search_fields = ('title',)
#     fields = ('title_uz', 'title_en', 'file', 'date', 'status', 'order',)
#
#
# @admin.register(Dissertatsiya_va_avtoref)
# class Dissertatsiya_va_avtorefAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
#     search_fields = ('title')
#     fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'status', 'order',)
#
#
# @admin.register(Dissertatsiya_fayllar)
# class Dissertatsiya_fayllarAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
#     search_fields = ('title')
#     fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'base_file',
#               'status', 'order',)
#
#
@admin.register(Yosh_olimlar)
class Yosh_olimlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'order',)

#
# @admin.register(Yosh_olimlar_azolari)
# class Yosh_olimlar_azolariAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
#     search_fields = ('title',)
#     fields = ('title_uz', 'title_en', 'position_uz',  'position_en', 'degree_uz',
#               'degree_en', 'contact', 'email', 'file', 'status', 'order',)
#
#
# @admin.register(Maruzalar)
# class MaruzalarAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
#     search_fields = ('title',)
#     fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz',
#               'subcontent_en', 'file', 'data', 'status', 'order',)




@admin.register(Azolar)
class AzolarAdmin(admin.ModelAdmin):
    list_display = ['name', 'shifr', 'ish_joy', 'lavozim', 'created_at', 'updated_at', 'order',]
    search_fields = ('name',)
    fields = ['name_uz', 'name_en', 'shifr', 'ish_joy_uz', 'ish_joy_en', 'lavozim_uz', 'lavozim_en',
              'ilmiy_darajasi_uz', 'ilmiy_darajasi_en', 'ilmiy_unvoni_uz', 'ilmiy_unvoni_en', 'status', 'order',]


@admin.register(DissertatsiyaIshlar)
class DissertatsiyaIshlarAdmin(admin.ModelAdmin):
    list_display = ['title', 'isAccepted', 'created_at', 'updated_at', 'order']
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'file', 'isAccepted', 'status', 'order',]


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'updated_at', 'order', 'status',]
    filter_horizontal = ('azolar', 'dissertatsiya_ishlar')
    fields = ['azolar', 'content_uz', 'content_en', 'dissertatsiya_ishlar', 'status', 'order',]
