from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from doktarantura.models import Qabul_tartibi, Malakaviy_imtihon, Doktarantura
from xalqaro_aloqalar.pagination import ResultsSetPagination

from doktarantura.serializers import Qabul_tartibiSerializer, Malakaviy_imtihonSerializer, DoktaranturaSerializer


class Qabul_tartibiListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Qabul_tartibiSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Qabul_tartibi.objects.all().order_by('order')


@api_view(['GET'])
def qabul_tartibidetail(request, pk):
    qabul_tartibi = get_object_or_404(Qabul_tartibi, pk=pk)
    serializer = Qabul_tartibiSerializer(qabul_tartibi, context={'request': request})
    return Response(serializer.data)


class Malakaviy_imtihonListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Malakaviy_imtihonSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Malakaviy_imtihon.objects.all().order_by('order')


@api_view(['GET'])
def malakaviy_imtihondetail(request, pk):
    malakaviy_imtihon = get_object_or_404(Malakaviy_imtihon, pk=pk)
    serializer = Malakaviy_imtihonSerializer(malakaviy_imtihon, context={'request': request})
    return Response(serializer.data)


class DoktaranturaListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = DoktaranturaSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Doktarantura.objects.all().order_by('order')


@api_view(['GET'])
def doktaranturadetail(request, pk):
    doktarantura = get_object_or_404(Doktarantura, pk=pk)
    serializer = DoktaranturaSerializer(doktarantura, context={'request': request})
    return Response(serializer.data)