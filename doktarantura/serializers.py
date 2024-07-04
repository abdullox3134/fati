from .models import Qabul_tartibi, Malakaviy_imtihon, Doktarantura
from rest_framework import serializers


class Qabul_tartibiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qabul_tartibi
        fields = ('id', 'title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'file', 'status', 'order', 'created_at', 'updated_at',)


class Malakaviy_imtihonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Malakaviy_imtihon
        fields = ('id', 'title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'file', 'status', 'order', 'created_at', 'updated_at',)


class DoktaranturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doktarantura
        fields = ('id', 'title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'file', 'type', 'status', 'order', 'created_at', 'updated_at',)



