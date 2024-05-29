from rest_framework import serializers
from markazlar_va_bolimlar.models import Markazlar_bolimlar, Bolimlar_tarix, Tadqiqot, Rasm, Video, Azolar


class Markazlar_bolimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Markazlar_bolimlar
        fields = ('id', 'title', 'content', 'file', 'status', 'order', 'created_at', 'updated_at',)


class Bolimlar_tarixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolimlar_tarix
        fields = ('id', 'title', 'content', 'file', 'status', 'center_id', 'order', 'created_at',
                  'updated_at',)


class TadqiqotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tadqiqot
        fields = ('id', 'title', 'content', 'file', 'status', 'center_id', 'order', 'created_at',
                  'updated_at',)


class AzolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Azolar
        fields = ('id', 'title', 'content', 'birth', 'sphere', 'center_id', 'position', 'academic_degree',
                  'email', 'file', 'status', 'order', 'created_at', 'updated_at',)


class RasmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rasm
        fields = ('id', 'title', 'content', 'image', 'center_id', 'file', 'status', 'order',
                  'created_at', 'updated_at',)


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'content', 'link', 'file', 'center_id', 'status', 'order', 'created_at',
                  'updated_at',)
