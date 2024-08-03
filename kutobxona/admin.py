from django.contrib import admin
from kutobxona.models import Category, Archive, DissertationsAndAbstracts, Editor, Requirements


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'status', 'order',)


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'sub_content_uz',
              'sub_content_en', 'file', 'base_file', 'status', 'order',)


@admin.register(DissertationsAndAbstracts)
class DissertationsAndAbstractsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'category', 'content_uz', 'content_en',
              'image', 'file', 'status', 'order',)


@admin.register(Editor)
class EditorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'email', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'position_uz', 'position_en', 'degree_uz', 'degree_en', 'sphere_uz', 'sphere_en',
              'content_uz', 'content_en', 'email', 'file', 'status', 'order',)


@admin.register(Requirements)
class RequirementsAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'sub_content_uz',
              'sub_content_en', 'file', 'status', 'order',)

