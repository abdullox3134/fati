# from rest_framework import serializers
# from kutobxona.models import Category, Archive, DissertationsAndAbstracts, Editor, Requirements
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'title_uz', 'title_en',  'status', 'order', 'created_at', 'updated_at',)
#
#
# class ArchiveSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Archive
#         fields = ('id', 'title_uz', 'title_en',  'content_uz', 'content_en',  'sub_content', 'file', 'base_file',
#                   'status', 'order', 'created_at', 'updated_at',)
#
#
#
# class DissertationsAndAbstractsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DissertationsAndAbstracts
#         fields = ('id', 'title_uz', 'title_en',  'category', 'content_uz',  'content_en',  'image', 'file', 'status',
#                   'order', 'created_at', 'updated_at',)
#
#
# class EditorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Editor
#         fields = ('id', 'title_uz', 'title_en', 'position_en', 'degree_uz', 'degree_en', 'sphere_uz', 'sphere_en',
#                   'content_uz', 'content_en',  'email', 'file', 'status', 'order', 'created_at', 'updated_at',)
#
#
# class RequirementsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Requirements
#         fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en',  'sub_content', 'file', 'status', 'order',
#                   'created_at', 'updated_at')
from rest_framework import serializers
from kutobxona.models import Maqola, Tahrirchi, ArxivSon, Avtoreferat, Manba, ElektronKitob


class TahrirchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tahrirchi
        fields = ['title_uz', 'title_en', 'ish_joyi', 'lavozimi', 'created_at', 'updated_at']


class ArxivSonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArxivSon
        fields = ['content', 'file_url', 'created_at', 'updated_at']


class MaqolaSerializer(serializers.ModelSerializer):
    tahrirchilar = TahrirchiSerializer(many=True, read_only=True)
    arxiv_sonlar = ArxivSonSerializer(many=True, read_only=True)

    class Meta:
        model = Maqola
        fields = ['content', 'tahrirchilar', 'arxiv_sonlar', 'created_at', 'updated_at']


class AvtoreferatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avtoreferat
        fields = ['title_uz', 'title_en', 'cover_img', 'file', 'created_at', 'updated_at']


class ElektronKitobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElektronKitob
        fields = ['title_uz', 'title_en', 'cover_img', 'file', 'created_at', 'updated_at']


class ManbaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manba
        fields = ['title_uz', 'title_en', 'cover_img', 'file', 'created_at', 'updated_at']
