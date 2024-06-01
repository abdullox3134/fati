from rest_framework import serializers
from kutobxona.models import Category, Archive, DissertationsAndAbstracts, Editor, Requirements


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'status', 'order', 'created_at', 'updated_at',)


class ArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = ('id', 'title', 'content', 'sub_content', 'file', 'base_file', 'status', 'order', 'created_at',
                  'updated_at',)


class DissertationsAndAbstractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DissertationsAndAbstracts
        fields = ('id', 'title', 'category', 'content', 'image', 'file', 'status', 'order', 'created_at', 'updated_at',)


class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = ('id', 'title', 'position', 'degree', 'sphere', 'content', 'email', 'file', 'status', 'order',
                  'created_at', 'updated_at',)


class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = ('id', 'title', 'content', 'sub_content', 'file', 'status', 'order', 'created_at', 'updated_at',)
