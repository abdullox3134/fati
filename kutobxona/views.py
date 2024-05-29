from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from kutobxona.models import Category, DissertationsAndAbstracts, Archive, Editor, Requirements
from kutobxona.serializers import CategorySerializer, DissertationsAndAbstractsSerializer, ArchiveSerializer, EditorSerializer, RequirementsSerializer
from xalqaro_aloqalar.pagination import ResultsSetPagination


class CategoryListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = CategorySerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Category.objects.all().order_by('order')


@api_view(['GET'])
def categorydetail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category, context={'request': request})
    return Response(serializer.data)


class DissertationsAndAbstractsListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = DissertationsAndAbstractsSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return DissertationsAndAbstracts.objects.all().order_by('order')


@api_view(['GET'])
def dissertations_detail(request, pk):
    dissertations = get_object_or_404(DissertationsAndAbstracts, pk=pk)
    serializer = DissertationsAndAbstractsSerializer(dissertations, context={'request': request})
    return Response(serializer.data)


class ArchiveListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ArchiveSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Archive.objects.all().order_by('order')


@api_view(['GET'])
def archive_detail(request, pk):
    archive = get_object_or_404(Archive, pk=pk)
    serializer = ArchiveSerializer(archive, context={'request': request})
    return Response(serializer.data)


class EditorListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = EditorSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Editor.objects.all().order_by('order')


@api_view(['GET'])
def editor_detail(request, pk):
    editor = get_object_or_404(Editor, pk=pk)
    serializer = EditorSerializer(editor, context={'request': request})
    return Response(serializer.data)


class RequirementsListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = RequirementsSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Requirements.objects.all().order_by('order')


@api_view(['GET'])
def requirements_detail(request, pk):
    requirements = get_object_or_404(Requirements, pk=pk)
    serializer = RequirementsSerializer(requirements, context={'request': request})
    return Response(serializer.data)

