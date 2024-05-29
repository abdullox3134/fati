from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from qoshimcha_malumotlar.models import Institut_tarixi, Memory_hujjatlar, Elonlar, Aloqa, Karusel, Rahbariyat, \
    Tashkiliy_tuzulma, Yangiliklar, Havolalar
from qoshimcha_malumotlar.serializers import Institut_tarixiSerializer, Memory_hujjatlarSerializer, ElonlarSerializer, \
    AloqaSerializer, KaruselSerializer, RahbariyatSerializer, Tashkiliy_tuzulmaSerializer, YangiliklarSerializer, \
    HavolalarSerializer
from xalqaro_aloqalar.pagination import ResultsSetPagination


class Institut_tarixiListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Institut_tarixiSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Institut_tarixi.objects.all().order_by('order')


@api_view(['GET'])
def institut_tarixidetail(request, pk):
    institut_tarixi = get_object_or_404(Institut_tarixi, pk=pk)
    serializer = Institut_tarixiSerializer(institut_tarixi, context={'request': request})
    return Response(serializer.data)


class Memory_hujjatlarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Memory_hujjatlarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Memory_hujjatlar.objects.all().order_by('order')


@api_view(['GET'])
def memory_hujjatlardetail(request, pk):
    memory_hujjatlar = get_object_or_404(Memory_hujjatlar, pk=pk)
    serializer = Memory_hujjatlarSerializer(memory_hujjatlar, context={'request': request})
    return Response(serializer.data)


class ElonlarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ElonlarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Elonlar.objects.all().order_by('order')


@api_view(['GET'])
def elonlardetail(request, pk):
    elonlar = get_object_or_404(Elonlar, pk=pk)
    serializer = ElonlarSerializer(elonlar, context={'request': request})
    return Response(serializer.data)


class AloqaListView(ListAPIView):
    search_fields = ['phone']
    filter_backends = (filters.SearchFilter,)
    serializer_class = AloqaSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Aloqa.objects.all().order_by('order')


@api_view(['GET'])
def aloqadetail(request, pk):
    aloqa = get_object_or_404(Aloqa, pk=pk)
    serializer = AloqaSerializer(aloqa, context={'request': request})
    return Response(serializer.data)


class KaruselListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = KaruselSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Karusel.objects.all().order_by('order')


@api_view(['GET'])
def karuseldetail(request, pk):
    karusel = get_object_or_404(Karusel, pk=pk)
    serializer = KaruselSerializer(karusel, context={'request': request})
    return Response(serializer.data)


class RahbariyatListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = RahbariyatSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Rahbariyat.objects.all().order_by('order')


@api_view(['GET'])
def rahbariyatdetail(request, pk):
    rahbariyat = get_object_or_404(Rahbariyat, pk=pk)
    serializer = RahbariyatSerializer(rahbariyat, context={'request': request})
    return Response(serializer.data)


class Tashkiliy_tuzulmaListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Tashkiliy_tuzulmaSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Tashkiliy_tuzulma.objects.all().order_by('order')


@api_view(['GET'])
def tashkiliy_tuzulmadetail(request, pk):
    tashkiliy_tuzulma = get_object_or_404(Tashkiliy_tuzulma, pk=pk)
    serializer = Tashkiliy_tuzulmaSerializer(tashkiliy_tuzulma, context={'request': request})
    return Response(serializer.data)


class YangiliklarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = YangiliklarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Yangiliklar.objects.all().order_by('order')


@api_view(['GET'])
def yangiliklardetail(request, pk):
    yangiliklar = get_object_or_404(Yangiliklar, pk=pk)
    serializer = YangiliklarSerializer(yangiliklar, context={'request': request})
    return Response(serializer.data)


class HavolalarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = HavolalarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Havolalar.objects.all().order_by('order')


@api_view(['GET'])
def havolalardetail(request, pk):
    havolalar = get_object_or_404(Havolalar, pk=pk)
    serializer = HavolalarSerializer(havolalar, context={'request': request})
    return Response(serializer.data)