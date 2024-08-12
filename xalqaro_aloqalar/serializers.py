from rest_framework import serializers
from xalqaro_aloqalar.models import Xamkor_tashkilot, Xamkor_loihalar, Xalqaro_sayohatlar
# serializers.py
from .models import Tadqiqot, Kelganlar


class TadqiqotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tadqiqot
        fields = ['id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'img_file', 'status', 'order',
                  'created_at', 'updated_at', ]


class KelganlarSerializer(serializers.ModelSerializer):
    kelganlarlar = TadqiqotSerializer(many=True, read_only=True)

    class Meta:
        model = Kelganlar
        fields = ['id', 'tadqiqot', 'kelgan_yil', 'ism_uz', 'ism_en', 'ish_joy_uz', 'ish_joy_en', 'status',
                  'created_at', 'updated_at', 'order', 'kelganlarlar']


class Xamkor_tashkilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xamkor_tashkilot
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz',  'subcontent_en', 'file',
                  'status', 'order', 'created_at', 'updated_at',)


class Xamkor_loihalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xamkor_loihalar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz', 'subcontent_en', 'file',
                  'status', 'order', 'created_at', 'updated_at',)


# class Xalqaro_tadqiqotSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Xalqaro_tadqiqot
#         fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz', 'subcontent_en', 'file',
#                   'status', 'order', 'created_at', 'updated_at',)


class Xalqaro_sayohatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xalqaro_sayohatlar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz',
                  'subcontent_en', 'file', 'status', 'order', 'created_at', 'updated_at',)





