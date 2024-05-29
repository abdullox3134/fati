from .models import Qabul_tartibi, Malakaviy_imtihon, Doktarantura
from rest_framework import serializers


class Qabul_tartibiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qabul_tartibi
        fields = ('id', 'title', 'content', 'file', 'status', 'order', 'created_at', 'updated_at',)


class Malakaviy_imtihonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Malakaviy_imtihon
        fields = ('id', 'title', 'content', 'file', 'status', 'order', 'created_at', 'updated_at',)


class DoktaranturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doktarantura
        fields = ('id', 'title', 'content', 'file', 'type', 'status', 'order', 'created_at', 'updated_at',)