from rest_framework import serializers

from seminar.models import Seminar_turlari, Seminar, Seminar_majlislari


class Seminar_turlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminar_turlari
        fields = ('id', 'title_uz', 'title_en', 'status', 'order', 'created_at', 'updated_at',)


class SeminarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminar
        fields = ('id', 'title_uz', 'title_en', 'subcontent_uz', 'subcontent_en', 'seminar_id', 'status', 'order',
                  'created_at', 'updated_at',)


class Seminar_majlislariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminar_majlislari
        fields = ('id', 'title_uz', 'title_en', 'content_en', 'content_uz', 'subcontent_uz', 'subcontent_en', 'file',
                  'data', 'seminar_id', 'status', 'order', 'created_at', 'updated_at',)

