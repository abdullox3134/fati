from rest_framework import serializers
from xalqaro_aloqalar.models import Xamkor_tashkilot, Xamkor_loihalar, Xalqaro_sayohatlar, xamkor_loyihalar_data
# serializers.py
from xalqaro_aloqalar.models import Tadqiqot, Kelganlar


class KelganlarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kelganlar
        fields = ['id', 'kelgan_yil', 'ism_uz', 'ism_en', 'ish_joy_uz', 'ish_joy_en', 'status',
                  'created_at', 'updated_at', 'order',]


class TadqiqotSerializer(serializers.ModelSerializer):
    tadqiqot = KelganlarSerializer(many=True, read_only=True)

    class Meta:
        model = Tadqiqot
        fields = ['id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'img_file', 'status', 'order',
                  'created_at', 'updated_at', 'tadqiqot',]


class Xamkor_tashkilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xamkor_tashkilot
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz',  'subcontent_en', 'file',
                  'status', 'order', 'created_at', 'updated_at',)


class xamkor_loyihalar_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = xamkor_loyihalar_data
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en',
                  'status', 'order', 'isCompleted', 'created_at', 'updated_at',)


class Xamkor_loihalarSerializer(serializers.ModelSerializer):
    xamkor_loiha = xamkor_loyihalar_dataSerializer(many=True, read_only=True)

    class Meta:
        model = Xamkor_loihalar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en',  'img_file', 'xamkor_loiha',
                  'status', 'order', 'created_at', 'updated_at')





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





