from rest_framework import serializers
from kutobxona.models import Category, Archive, DissertationsAndAbstracts, Editor, Requirements


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title_uz', 'title_ru', 'title_en',  'status', 'order', 'created_at', 'updated_at',)


class ArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = ('id', 'title_uz', 'title_ru', 'title_en',  'content_uz', 'content_ru', 'content_en',  'sub_content', 'file', 'base_file', 'status', 'order', 'created_at',
                  'updated_at',)


class DissertationsAndAbstractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DissertationsAndAbstracts
        fields = ('id', 'title_uz', 'title_ru', 'title_en',  'category', 'content_uz', 'content_ru', 'content_en',  'image', 'file', 'status', 'order', 'created_at', 'updated_at',)


class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = ('id', 'title_uz', 'title_ru', 'title_en',  'position', 'degree', 'sphere', 'content_uz', 'content_ru', 'content_en',  'email', 'file', 'status', 'order',
                  'created_at', 'updated_at',)


class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = ('id', 'title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en',  'sub_content', 'file', 'status', 'order', 'created_at', 'updated_at',)
