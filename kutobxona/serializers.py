from rest_framework import serializers
# from kutobxona.models import Category, Archive, DissertationsAndAbstracts, Editor, Requirements
from .models import Talablar
from .models import ArxivMenu, Arxiv

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
from rest_framework import serializers
from . models import Maqola, Tahrirchi, ArxivSon, Avtoreferat, Manba, ElektronKitob


class TalabalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talablar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en',  'sub_content_uz', 'sub_content_uz', 'file',
                  'status', 'order', 'created_at', 'Updated_at')



class TahrirchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tahrirchi
        fields = ['title_uz', 'title_en', 'ish_joyi', 'lavozimi', 'status', 'order', 'created_at', 'Updated_at',]


class ArxivSonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArxivSon
        fields = ['content', 'file_url', 'status', 'order' 'created_at', 'Updated_at']


class MaqolaSerializer(serializers.ModelSerializer):
    tahrirchilar = TahrirchiSerializer(many=True, read_only=True)
    arxiv_sonlar = ArxivSonSerializer(many=True, read_only=True)

    class Meta:
        model = Maqola
        fields = ['content', 'tahrirchilar', 'arxiv_sonlar', 'status', 'order' 'created_at', 'Updated_at']


class AvtoreferatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avtoreferat
        fields = ['title_uz', 'title_en', 'cover_img', 'file', 'status', 'order' 'created_at', 'Updated_at']


class ElektronKitobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElektronKitob
        fields = ['title_uz', 'title_en', 'cover_img', 'file', 'status', 'order''created_at', 'Updated_at']


class ManbaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manba
        fields = ['title_uz', 'title_en', 'cover_img', 'file', 'status', 'order' 'created_at', 'Updated_at']


class ArxivMenuSerializer(serializers.ModelSerializer):
    # `many=True` to'g'ri, `read_only=True` to'g'ri

    class Meta:
        model = ArxivMenu
        field = ['id', 'davr_oraligi', 'content', 'status', 'order', 'created_at', 'Updated_at',]


class ArxivSerializer(serializers.ModelSerializer):
    arxiv_list = ArxivMenuSerializer(many=True, read_only=True)

    class Meta:
        model = Arxiv
        fields = ['id', 'yil', 'nashr_raqami', 'file_url', 'status', 'order', 'created_at', 'Updated_at', 'arxiv_list']


