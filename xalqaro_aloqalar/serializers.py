from rest_framework import serializers
from xalqaro_aloqalar.models import Xamkor_tashkilot, Xamkor_loihalar, Xalqaro_tadqiqot, Xalqaro_sayohatlar


class Xamkor_tashkilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xamkor_tashkilot
        fields = ('id', 'title', 'content', 'subcontent', 'file', 'status', 'order', 'created_at', 'updated_at',)


class Xamkor_loihalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xamkor_loihalar
        fields = ('id', 'title', 'content', 'subcontent', 'file', 'status', 'order', 'created_at', 'updated_at',)


class Xalqaro_tadqiqotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xalqaro_tadqiqot
        fields = ('id', 'title', 'content', 'subcontent', 'file', 'status', 'order', 'created_at', 'updated_at',)


class Xalqaro_sayohatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xalqaro_sayohatlar
        fields = ('id', 'title', 'content', 'subcontent', 'file', 'status', 'order', 'created_at', 'updated_at',)