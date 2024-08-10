# from rest_framework import serializers
#
# from kengashlar.models import Institut_ken_azolari, Ilmiy_kengash_majlis, Qabul_korib_gan_dissertatsiya, \
#     Shifr_va_passport, Dissertatsiya_va_avtoref, Dissertatsiya_fayllar, Yosh_olimlar, Yosh_olimlar_azolari, Maruzalar
#
#
# class Institut_ken_azolariSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Institut_ken_azolari
#         fields = ('id', 'title_uz', 'title_en', 'file', 'status', 'order', 'created_at', 'updated_at',)
#
#
# class Ilmiy_kengash_majlisSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ilmiy_kengash_majlis
#         fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en',  'subcontent', 'file', 'date', 'status', 'order', 'created_at',
#                   'updated_at',)
#
#
# class Qabul_korib_gan_dissertatsiyaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Qabul_korib_gan_dissertatsiya
#         fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'order', 'created_at', 'updated_at',)
#
#
# class Shifr_va_passportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Shifr_va_passport
#         fields = ('id', 'title_uz', 'title_en', 'file', 'date', 'status', 'order', 'created_at', 'updated_at',)
#
#
# class Dissertatsiya_va_avtorefSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Dissertatsiya_va_avtoref
#         fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'status', 'order', 'created_at', 'updated_at',)
#
#
# class Dissertatsiya_fayllarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Dissertatsiya_fayllar
#         fields = ('id', 'title_uz', 'title_en', 'content_uz',  'content_en', 'file', 'base_file', 'status', 'order', 'created_at', 'updated_at',)
#
#
# class Yosh_olimlarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Yosh_olimlar
#         fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'order', 'created_at', 'updated_at',)
#
#
# class Yosh_olimlar_azolariSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Yosh_olimlar_azolari
#         fields = ('id', 'title_uz', 'title_en', 'position_uz', 'position_en', 'degree_uz', 'degree_en', 'contact', 'email', 'file', 'status', 'order', 'created_at',
#                   'updated_at',)
#
#
# class MaruzalarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Maruzalar
#         fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent', 'file', 'data', 'status', 'order', 'created_at',
#                   'updated_at',)

from rest_framework import serializers
from .models import Azolar, DissertatsiyaIshlar, Content


class AzolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Azolar
        fields = ['id', 'name_uz', 'name_en', 'shifr', 'ish_joy_uz', 'ish_joy_en', 'lavozim_uz', 'lavozim_en',
                  'ilmiy_darajasi_uz', 'ilmiy_darajasi_en', 'ilmiy_unvoni_uz', 'ilmiy_unvoni_en',
                  'created_at', 'updated_at', ]


class DissertatsiyaIshlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = DissertatsiyaIshlar
        fields = ['id', 'title_uz', 'title_en', 'file', 'isAccepted', 'created_at', 'updated_at', ]


class ContentSerializer(serializers.ModelSerializer):
    azolar = AzolarSerializer(many=True, read_only=True)
    dissertatsiya_ishlar = DissertatsiyaIshlarSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = ['id', 'azolar', 'content_uz', 'content_en', 'dissertatsiya_ishlar', 'created_at', 'updated_at', ]
