# from django.contrib import admin
# from .models import Markazlar_bolimlar, Azolar, Bolimlar_tarix, Rasm, Azolarsub
#
#
# @admin.register(Markazlar_bolimlar)
# class markazlar_bolimlars(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
#     fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'order',]
#
#
# @admin.register(Bolimlar_tarix)
# class Bolimlar_tarixisub(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
#     fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'center_id', 'file',
#               'status', 'order', ]
#
#
# # @admin.register(Tadqiqot)
# # class Tadqiqotsub(admin.ModelAdmin):
# #     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
# #     fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'center_id', 'file',
# #               'status', 'order', ]
# #
#
# class Azolarsubadmin(admin.TabularInline):
#     model = Azolarsub
#     fields = ['title_uz', 'title_en', 'link']
#
#
# @admin.register(Azolar)
# class AzolarAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
#     inlines = [Azolarsubadmin]
#     fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'birth', 'sphere', 'position_uz', 'position_en',
#               'academic_degree_uz',  'academic_degree_en', 'email', 'file', 'center_id', 'status', 'order',)
#
#
#
#
# @admin.register(Rasm)
# class Rasmsub(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
#     fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'center_id',
#               'file', 'status', 'order', ]


# @admin.register(Video)
# class Videosub(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
#     fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'center_id', 'link', 'file',
#               'status', 'order', ]
#

from django.contrib import admin
from .models import Fotogalereya, Slider, Xodimlar, MarkazlarBolimlar


class FotogalereyaAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_url')


class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_url')


class XodimlarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lavozim', 'ilmiy_daraja')
    search_fields = ('name',)
    fields = ('name_uz', 'name_en', 'lavozim_uz', 'lavozim_en', 'ilmiy_daraja_uz', 'ilmiy_daraja_en',)


class MarkazlarBolimlarAdmin(admin.ModelAdmin):
    list_display = ('status', 'order', 'created_at', 'updated_at')
    search_fields = ('status', 'order')
    list_filter = ('status', 'created_at', 'updated_at')
    filter_horizontal = ('xodimlar', 'fotogalereya', 'slider')
    fields = ('tarix_uz', 'tarix_en', 'xodimlar', 'fotogalereya', 'slider', 'status', 'order',)


admin.site.register(Fotogalereya, FotogalereyaAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Xodimlar, XodimlarAdmin)
admin.site.register(MarkazlarBolimlar, MarkazlarBolimlarAdmin)
