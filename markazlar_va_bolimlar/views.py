# from rest_framework.decorators import api_view
# from rest_framework.generics import ListAPIView
# from rest_framework import filters
# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
#
# from markazlar_va_bolimlar.models import Markazlar_bolimlar, Bolimlar_tarix,  Azolar, Rasm
# from markazlar_va_bolimlar.serializers import Markazlar_bolimlarSerializer, Bolimlar_tarixSerializer, \
#      AzolarSerializer, RasmSerializer
# from xalqaro_aloqalar.pagination import ResultsSetPagination
#
#
# class Markazlar_bolimlarListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = Markazlar_bolimlarSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Markazlar_bolimlar.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def markazlar_bolimlardetail(request, pk):
#     markazlar_bolimlar = get_object_or_404(Markazlar_bolimlar, pk=pk)
#     serializer = Markazlar_bolimlarSerializer(markazlar_bolimlar, context={'request': request})
#     return Response(serializer.data)
#
#
# class Bolimlar_tarixListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = Bolimlar_tarixSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Bolimlar_tarix.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def bolimlar_tarixdetail(request, pk):
#     bolimlar_tarix = get_object_or_404(Bolimlar_tarix, pk=pk)
#     serializer = Bolimlar_tarixSerializer(bolimlar_tarix, context={'request': request})
#     return Response(serializer.data)


# class TadqiqotListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = TadqiqotSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Tadqiqot.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def tadqiqotdetail(request, pk):
#     tadqiqot = get_object_or_404(Tadqiqot, pk=pk)
#     serializer = TadqiqotSerializer(tadqiqot, context={'request': request})
#     return Response(serializer.data)


# class AzolarListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = AzolarSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Azolar.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def azolardetail(request, pk):
#     azolar = get_object_or_404(Azolar, pk=pk)
#     serializer = AzolarSerializer(azolar, context={'request': request})
#     return Response(serializer.data)
#
#
# class RasmListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = RasmSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Rasm.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def rasmdetail(request, pk):
#     rasm = get_object_or_404(Rasm, pk=pk)
#     serializer = RasmSerializer(rasm, context={'request': request})
#     return Response(serializer.data)


# class VideoListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = VideoSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Video.objects.all().order_by('order')
#

# @api_view(['GET'])
# def videodetail(request, pk):
#     video = get_object_or_404(Video, pk=pk)
#     serializer = VideoSerializer(video, context={'request': request})
#     return Response(serializer.data)
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from .models import Fotogalereya, Slider, Xodimlar, MarkazlarBolimlar
from .serializers import FotogalereyaSerializer, SliderSerializer, XodimlarSerializer, MarkazlarBolimlarSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class FotogalereyaListCreate(ListAPIView):
    queryset = Fotogalereya.objects.all()
    serializer_class = FotogalereyaSerializer


@api_view(['GET'])
def FotogalereyaDetail(request, pk):
    fotogalereya = get_object_or_404(Fotogalereya, pk=pk)
    serializer = FotogalereyaSerializer(fotogalereya, context={'request': request})
    return Response(serializer.data)


class SliderListCreate(ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


@api_view(['GET'])
def SliderDetail(request, pk):
    slider = get_object_or_404(Slider, pk=pk)
    serializer = SliderSerializer(slider, context={'request': request})
    return Response(serializer.data)


class XodimlarListCreate(ListAPIView):
    queryset = Xodimlar.objects.all()
    serializer_class = XodimlarSerializer


@api_view(['GET'])
def XodimlarDetail(request, pk):
    xodimlar = get_object_or_404(Xodimlar, pk=pk)
    serializer = XodimlarSerializer(xodimlar, context={'request': request})
    return Response(serializer.data)


class MarkazlarBolimlarListCreate(ListAPIView):
    queryset = MarkazlarBolimlar.objects.all()
    serializer_class = MarkazlarBolimlarSerializer


@api_view(['GET'])
def MarkazlarBolimlarDetail(request, pk):
    markazlarBolimlar = get_object_or_404(MarkazlarBolimlar, pk=pk)
    serializer = MarkazlarBolimlarSerializer(markazlarBolimlar, context={'request': request})
    return Response(serializer.data)
