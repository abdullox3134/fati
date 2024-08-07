# from django.urls import path
#
# from kutobxona.views import CategoryListView, categorydetail, archive_detail, editor_detail, requirements_detail, dissertations_detail, ArchiveListView, EditorListView, RequirementsListView, DissertationsAndAbstractsListView
#
# urlpatterns = [
#     path('category_list/', CategoryListView.as_view(), name='category_list'),
#     path('category_detail/<int:pk>/', categorydetail, name='category_detail'),
#
#     path('archive_list/', ArchiveListView.as_view(), name='archive_list'),
#     path('archive_detail/<int:pk>/', archive_detail, name='archive_detail'),
#
#     path('editor_list/', EditorListView.as_view(), name='editor_list'),
#     path('editor_detail/<int:pk>/', editor_detail, name='editor_detail'),
#
#     path('requirements_list/', RequirementsListView.as_view(), name='requirements_list'),
#     path('requirements_detail/<int:pk>/', requirements_detail, name='requirements_detail'),
#
#     path('dissertations_list/', DissertationsAndAbstractsListView.as_view(), name='dissertations_list'),
#     path('dissertations_detail/<int:pk>/', dissertations_detail, name='dissertations_detail'),
# ]

from django.urls import path
from .views import (
    MaqolaListCreateView,
    maqola_detail_view,
    TahrirchiListCreateView,
    tahrirchi_detail_view,
    ArxivSonListCreateView,
    arxiv_son_detail_view,
    AvtoreferatListCreateView,
    avtoreferat_detail_view,
    ElektronKitobListCreateView,
    elektron_kitob_detail_view,
    ManbaListCreateView,
    manba_detail_view,

)


from django.urls import path
from .views import MaqolaListCreateView, maqola_detail_view, TahrirchiListCreateView, ArxivSonListCreateView


urlpatterns = [
    path('maqolalar/', MaqolaListCreateView.as_view(), name='maqola-list'),
    path('maqolalar/<int:pk>/', maqola_detail_view, name='maqola-detail'),

    path('tahrirchilar/', TahrirchiListCreateView.as_view(), name='tahrirchi-list'),
    path('arxiv_sonlar/', ArxivSonListCreateView.as_view(), name='arxiv-son-list'),

    path('avtoreferat/', AvtoreferatListCreateView.as_view(), name='avtoreferat-list'),
    path('avtoreferat/', avtoreferat_detail_view, name='avtoreferat-detail'),

    path('elektronKitob/', ElektronKitobListCreateView.as_view(), name='elektronKitob-list'),
    path('elektronKitob/', elektron_kitob_detail_view, name='elektronKitob-detail'),

    path('manba/', ManbaListCreateView.as_view(), name='Manba-list'),
    path('Manba/', manba_detail_view, name='Manba-detail'),



]

