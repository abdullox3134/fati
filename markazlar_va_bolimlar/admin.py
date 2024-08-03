from django.contrib import admin
from .models import Markazlar_bolimlar, Azolar, Bolimlar_tarix, Rasm, Azolarsub


@admin.register(Markazlar_bolimlar)
class markazlar_bolimlars(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'order',]


@admin.register(Bolimlar_tarix)
class Bolimlar_tarixisub(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'center_id', 'file',
              'status', 'order', ]


# @admin.register(Tadqiqot)
# class Tadqiqotsub(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
#     fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'center_id', 'file',
#               'status', 'order', ]
#

class Azolarsubadmin(admin.TabularInline):
    model = Azolarsub
    fields = ['title_uz', 'title_en', 'link']


@admin.register(Azolar)
class AzolarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    inlines = [Azolarsubadmin]
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'birth', 'sphere', 'position_uz', 'position_en',
              'academic_degree_uz',  'academic_degree_en', 'email', 'file', 'center_id', 'status', 'order',)




@admin.register(Rasm)
class Rasmsub(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'center_id',
              'file', 'status', 'order', ]


# @admin.register(Video)
# class Videosub(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
#     fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'center_id', 'link', 'file',
#               'status', 'order', ]
#
