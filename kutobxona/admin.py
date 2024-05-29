from django.contrib import admin

from kutobxona.models import Category, Archive, DissertationsAndAbstracts, Editor, Requirements


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'image', 'file', 'base_file', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)


@admin.register(DissertationsAndAbstracts)
class DissertationsAndAbstractsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'image', 'file', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    
    
@admin.register(Editor)
class EditorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'image', 'email', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    
    
@admin.register(Requirements)
class RequirementsAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'image', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
