# from rest_framework.decorators import api_view
# from rest_framework.generics import ListAPIView
# from rest_framework import filters
# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
#
# from kutobxona.models import Category, DissertationsAndAbstracts, Archive, Editor, Requirements
# from kutobxona.serializers import CategorySerializer, DissertationsAndAbstractsSerializer, ArchiveSerializer, EditorSerializer, RequirementsSerializer
# from xalqaro_aloqalar.pagination import ResultsSetPagination
#
#
# class CategoryListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = CategorySerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Category.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def categorydetail(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     serializer = CategorySerializer(category, context={'request': request})
#     return Response(serializer.data)
#
#
# class DissertationsAndAbstractsListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = DissertationsAndAbstractsSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return DissertationsAndAbstracts.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def dissertations_detail(request, pk):
#     dissertations = get_object_or_404(DissertationsAndAbstracts, pk=pk)
#     serializer = DissertationsAndAbstractsSerializer(dissertations, context={'request': request})
#     return Response(serializer.data)
#
#
# class ArchiveListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = ArchiveSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Archive.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def archive_detail(request, pk):
#     archive = get_object_or_404(Archive, pk=pk)
#     serializer = ArchiveSerializer(archive, context={'request': request})
#     return Response(serializer.data)
#
#
# class EditorListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = EditorSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Editor.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def editor_detail(request, pk):
#     editor = get_object_or_404(Editor, pk=pk)
#     serializer = EditorSerializer(editor, context={'request': request})
#     return Response(serializer.data)
#
#
# class RequirementsListView(ListAPIView):
#     search_fields = ['title']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = RequirementsSerializer
#     pagination_class = ResultsSetPagination
#
#     def get_queryset(self):
#         return Requirements.objects.all().order_by('order')
#
#
# @api_view(['GET'])
# def requirements_detail(request, pk):
#     requirements = get_object_or_404(Requirements, pk=pk)
#     serializer = RequirementsSerializer(requirements, context={'request': request})
#     return Response(serializer.data)
#
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from kutobxona.models import Maqola, Tahrirchi, ArxivSon, Manba, Avtoreferat, ElektronKitob
from .serializers import (MaqolaSerializer, TahrirchiSerializer, ArxivSonSerializer,
                          AvtoreferatSerializer, ElektronKitobSerializer, ManbaSerializer)
from .pagination import ResultsSetPagination


class MaqolaListCreateView(ListAPIView):
    queryset = Maqola.objects.all()
    serializer_class = MaqolaSerializer
    pagination_class = ResultsSetPagination


@api_view(['GET'])
def maqola_detail_view(request, pk):
    maqola = get_object_or_404(Maqola, pk=pk)
    serializer = MaqolaSerializer(maqola, context={'request': request})
    return Response(serializer.data)


class TahrirchiListCreateView(ListAPIView):
    queryset = Tahrirchi.objects.all()
    serializer_class = TahrirchiSerializer
    pagination_class = ResultsSetPagination


@api_view(['GET'])
def tahrirchi_detail_view(request, pk):
    tahrirchi = get_object_or_404(Tahrirchi, pk=pk)
    serializer = TahrirchiSerializer(tahrirchi, context={'request': request})
    return Response(serializer.data)


class ArxivSonListCreateView(ListAPIView):
    queryset = ArxivSon.objects.all()
    serializer_class = ArxivSonSerializer
    pagination_class = ResultsSetPagination


@api_view(['GET'])
def arxiv_son_detail_view(request, pk):
    arxiv_son = get_object_or_404(ArxivSon, pk=pk)
    serializer = ArxivSonSerializer(arxiv_son, context={'request': request})
    return Response(serializer.data)


class AvtoreferatListCreateView(ListAPIView):
    queryset = Avtoreferat.objects.all()
    serializer_class = AvtoreferatSerializer
    pagination_class = ResultsSetPagination


@api_view(['GET'])
def avtoreferat_detail_view(request, pk):
    avtoreferat = get_object_or_404(Avtoreferat, pk=pk)
    serializer = AvtoreferatSerializer(avtoreferat, context={'request': request})
    return Response(serializer.data)


class ElektronKitobListCreateView(ListAPIView):
    queryset = ElektronKitob.objects.all()
    serializer_class = ElektronKitobSerializer
    pagination_class = ResultsSetPagination


@api_view(['GET'])
def elektron_kitob_detail_view(request, pk):
    elektron_kitob = get_object_or_404(ElektronKitob, pk=pk)
    serializer = ElektronKitobSerializer(elektron_kitob, context={'request': request})
    return Response(serializer.data)


class ManbaListCreateView(ListAPIView):
    queryset = Manba.objects.all()
    serializer_class = ManbaSerializer
    pagination_class = ResultsSetPagination


@api_view(['GET'])
def manba_detail_view(request, pk):
    manba = get_object_or_404(Manba, pk=pk)
    serializer = ManbaSerializer(manba, context={'request': request})
    return Response(serializer.data)


