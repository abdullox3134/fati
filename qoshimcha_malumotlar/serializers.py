from rest_framework import serializers

from qoshimcha_malumotlar.models import Institut_tarixi, Aloqa, Karusel, Rahbariyat, Tashkiliy_tuzulma, Yangiliklar, \
     Havolalar


class Institut_tarixiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institut_tarixi
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz', 'subcontent_en', 'file',
                  'base_file', 'status', 'order', 'created_at', 'updated_at',)


# class Memory_hujjatlarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Memory_hujjatlar
#         fields = ('id', 'title_uz', 'title_ru', 'title_en', 'file', 'status', 'order', 'created_at', 'updated_at',)
#
#
# class ElonlarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Elonlar
#         fields = ('id', 'title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'file',
#         'status', 'type', 'order', 'created_at', 'updated_at',)


class AloqaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aloqa
        fields = ('id', 'faks', 'email', 'phone', 'adress', 'lat', 'long', 'youtube', 'telegram', 'instagram',
                  'facebook', 'status', 'order', 'created_at', 'updated_at',)


class KaruselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karusel
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'link', 'order',
                  'created_at', 'updated_at',)


class RahbariyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rahbariyat
        fields = ('id', 'title_uz', 'title_en', 'position', 'degree', 'contact', 'days', 'image', 'status', 'order',
                  'created_at', 'updated_at',)


class Tashkiliy_tuzulmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tashkiliy_tuzulma
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'order', 'created_at',
                  'updated_at',)


class YangiliklarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangiliklar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz', 'subcontent_en', 'file',
                  'status', 'order', 'created_at', 'updated_at',)


class HavolalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Havolalar
        fields = ('id', 'title_uz', 'title_en', 'file', 'link', 'status', 'order', 'created_at', 'updated_at',)


