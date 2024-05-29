from django.urls import path

from kutobxona.views import CategoryListView, categorydetail, archive_detail, editor_detail, requirements_detail, dissertations_detail, ArchiveListView, EditorListView, RequirementsListView, DissertationsAndAbstractsListView

urlpatterns = [
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('category_detail/<int:pk>/', categorydetail, name='category_detail'),

    path('archive_list/', ArchiveListView.as_view(), name='archive_list'),
    path('archive_detail/<int:pk>/', archive_detail, name='archive_detail'),

    path('editor_list/', EditorListView.as_view(), name='editor_list'),
    path('editor_detail/<int:pk>/', editor_detail, name='editor_detail'),
    
    path('requirements_list/', RequirementsListView.as_view(), name='requirements_list'),
    path('requirements_detail/<int:pk>/', requirements_detail, name='requirements_detail'),
    
    path('dissertations_list/', DissertationsAndAbstractsListView.as_view(), name='dissertations_list'),
    path('dissertations_detail/<int:pk>/', dissertations_detail, name='dissertations_detail'),
]