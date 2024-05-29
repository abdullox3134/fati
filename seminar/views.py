from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from seminar.models import Seminar_turlari, Seminar, Seminar_majlislari
from seminar.serializers import Seminar_turlariSerializer, SeminarSerializer, Seminar_majlislariSerializer
from xalqaro_aloqalar.pagination import ResultsSetPagination


class Seminar_turlariListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Seminar_turlariSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Seminar_turlari.objects.all().order_by('order')


@api_view(['GET'])
def seminar_turlaridetail(request, pk):
    seminar_turlari = get_object_or_404(Seminar_turlari, pk=pk)
    serializer = Seminar_turlariSerializer(seminar_turlari, context={'request': request})
    return Response(serializer.data)


class SeminarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = SeminarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Seminar.objects.all().order_by('order')


@api_view(['GET'])
def seminardetail(request, pk):
    seminar = get_object_or_404(Seminar, pk=pk)
    serializer = SeminarSerializer(seminar, context={'request': request})
    return Response(serializer.data)


class Seminar_majlislariListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Seminar_majlislariSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Seminar_majlislari.objects.all().order_by('order')


@api_view(['GET'])
def seminar_majlislaridetail(request, pk):
    seminar_majlislari = get_object_or_404(Seminar_majlislari, pk=pk)
    serializer = Seminar_majlislariSerializer(seminar_majlislari, context={'request': request})
    return Response(serializer.data)