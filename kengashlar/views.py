
#
# from kengashlar.models import Institut_ken_azolari, Ilmiy_kengash_majlis, Qabul_korib_gan_dissertatsiya, \
#     Shifr_va_passport, Dissertatsiya_va_avtoref, Dissertatsiya_fayllar, Yosh_olimlar, Yosh_olimlar_azolari, Maruzalar
# from kengashlar.serializers import Institut_ken_azolariSerializer, Ilmiy_kengash_majlisSerializer, \
#     Qabul_korib_gan_dissertatsiyaSerializer, Shifr_va_passportSerializer, Dissertatsiya_va_avtorefSerializer, \
#     Dissertatsiya_fayllarSerializer, Yosh_olimlarSerializer, Yosh_olimlar_azolariSerializer, MaruzalarSerializer
# from xalqaro_aloqalar.pagination import ResultsSetPagination
#
#
# class Institut_ken_azolariListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = Institut_ken_azolariSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Institut_ken_azolari.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def institut_ken_azolaridetail(request, pk):
#     institut_ken_azolari = get_object_or_404(Institut_ken_azolari, pk=pk)
#     serializer = Institut_ken_azolariSerializer(institut_ken_azolari, context={'request': request})
#     return Response(serializer.data)
#
#
# class Ilmiy_kengash_majlisListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = Ilmiy_kengash_majlisSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Ilmiy_kengash_majlis.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def ilmiy_kengash_majlisdetail(request, pk):
#     ilmiy_kengash_majlis = get_object_or_404(Ilmiy_kengash_majlis, pk=pk)
#     serializer = Ilmiy_kengash_majlisSerializer(ilmiy_kengash_majlis, context={'request': request})
#     return Response(serializer.data)
#
#
# class Qabul_korib_gan_dissertatsiyaListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = Qabul_korib_gan_dissertatsiyaSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Qabul_korib_gan_dissertatsiya.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def qabul_korib_gan_dissertatsiyadetail(request, pk):
#     qabul_korib_gan_dissertatsiya = get_object_or_404(Qabul_korib_gan_dissertatsiya, pk=pk)
#     serializer = Qabul_korib_gan_dissertatsiyaSerializer(qabul_korib_gan_dissertatsiya, context={'request': request})
#     return Response(serializer.data)
#
#
# class Shifr_va_passportListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = Shifr_va_passportSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Shifr_va_passport.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def shifr_va_passportdetail(request, pk):
#     shifr_va_passport = get_object_or_404(Shifr_va_passport, pk=pk)
#     serializer = Shifr_va_passportSerializer(shifr_va_passport, context={'request': request})
#     return Response(serializer.data)
#
#
# class Dissertatsiya_va_avtorefListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = Dissertatsiya_va_avtorefSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Dissertatsiya_va_avtoref.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def dissertatsiya_va_avtorefdetail(request, pk):
#     dissertatsiya_va_avtoref = get_object_or_404(Dissertatsiya_va_avtoref, pk=pk)
#     serializer = Dissertatsiya_va_avtorefSerializer(dissertatsiya_va_avtoref, context={'request': request})
#     return Response(serializer.data)
#
#
# class Dissertatsiya_fayllarListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = Dissertatsiya_fayllarSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Dissertatsiya_fayllar.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def dissertatsiya_fayllardetail(request, pk):
#     dissertatsiya_fayllar = get_object_or_404(Dissertatsiya_fayllar, pk=pk)
#     serializer = Dissertatsiya_fayllarSerializer(dissertatsiya_fayllar, context={'request': request})
#     return Response(serializer.data)
#
#
# class Yosh_olimlarListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = Yosh_olimlarSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Yosh_olimlar.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def yosh_olimlardetail(request, pk):
#     yosh_olimlar = get_object_or_404(Yosh_olimlar, pk=pk)
#     serializer = Yosh_olimlarSerializer(yosh_olimlar, context={'request': request})
#     return Response(serializer.data)
#
#
# class Yosh_olimlar_azolariListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = Yosh_olimlar_azolariSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Yosh_olimlar_azolari.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def yosh_olimlar_azolaridetail(request, pk):
#     yosh_olimlar_azolari = get_object_or_404(Yosh_olimlar_azolari, pk=pk)
#     serializer = Yosh_olimlar_azolariSerializer(yosh_olimlar_azolari, context={'request': request})
#     return Response(serializer.data)
#
#
# class MaruzalarListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = MaruzalarSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Maruzalar.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def maruzalardetail(request, pk):
#     maruzalar = get_object_or_404(Maruzalar, pk=pk)
#     serializer = MaruzalarSerializer(maruzalar, context={'request': request})
#     return Response(serializer.data)
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Azolar, DissertatsiyaIshlar, Content
from .serializers import AzolarSerializer, DissertatsiyaIshlarSerializer, ContentSerializer

from rest_framework import generics

class AzolarListView(generics.ListAPIView):
    queryset = Azolar.objects.all()
    serializer_class = AzolarSerializer


@api_view(['GET'])
def Azolardetail(request, pk):
    azolar = get_object_or_404(Azolar, pk=pk)
    serializer = AzolarSerializer(azolar, context={'request': request})
    return Response(serializer.data)


class DissertatsiyaIshlarListView(ListAPIView):
    queryset = DissertatsiyaIshlar.objects.all()
    serializer_class = DissertatsiyaIshlarSerializer

@api_view(['GET'])
def DissertatsiyaIshlardetail(request, pk):
    azolar = get_object_or_404(DissertatsiyaIshlar, pk=pk)
    serializer = DissertatsiyaIshlarSerializer(azolar, context={'request': request})
    return Response(serializer.data)


class ContentListView(ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

@api_view(['GET'])
def Contentdetail(request, pk):
    content = get_object_or_404(Content, pk=pk)
    serializer = ContentSerializer(content, context={'request': request})
    return Response(serializer.data)



