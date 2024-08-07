# from django.urls import path
#
# from markazlar_va_bolimlar.views import Markazlar_bolimlarListView, markazlar_bolimlardetail, Bolimlar_tarixListView, \
#     bolimlar_tarixdetail, AzolarListView, azolardetail, RasmListView, rasmdetail
#
# urlpatterns = [
#     path('markazlar-bolimlar/', Markazlar_bolimlarListView.as_view(), name='markazlar_bolimlar-list'),
#     path('markazlar-bolimlar/<int:pk>/', markazlar_bolimlardetail, name='markazlar_bolimlar-detail'),
#
#     path('bolimlar-tarix/', Bolimlar_tarixListView.as_view(), name='bolimlar_tarix-list'),
#     path('bolimlar-tarix/<int:pk>/', bolimlar_tarixdetail, name='bolimlar_tarix-detail'),
#
#     # path('tadqiqot/', TadqiqotListView.as_view(), name='tadqiqot-list'),
#     # path('tadqiqot/<int:pk>/', tadqiqotdetail, name='tadqiqot-detail'),
#
#     path('azolar/', AzolarListView.as_view(), name='azolar-list'),
#     path('azolar/<int:pk>/', azolardetail, name='azolar-detail'),
#
#     path('rasm/', RasmListView.as_view(), name='rasm-list'),
#     path('rasm/<int:pk>/', rasmdetail, name='rasm-detail'),
#
# #     path('video/', VideoListView.as_view(), name='video-list'),
# #     path('video/<int:pk>/', videodetail, name='video-detail'),
#  ]

from django.urls import path
from .views import (
    FotogalereyaListCreate,
    FotogalereyaDetail,
    SliderListCreate,
    SliderDetail,
    XodimlarListCreate,
    XodimlarDetail,
    MarkazlarBolimlarListCreate,
    MarkazlarBolimlarDetail
)

urlpatterns = [
    path('fotogalereya/', FotogalereyaListCreate.as_view(), name='fotogalereya-list-create'),
    path('fotogalereya/<int:pk>/', FotogalereyaDetail, name='fotogalereya-detail'),

    path('slider/', SliderListCreate.as_view(), name='slider-list-create'),
    path('slider/<int:pk>/', SliderDetail, name='slider-detail'),

    path('xodimlar/', XodimlarListCreate.as_view(), name='xodimlar-list-create'),
    path('xodimlar/<int:pk>/', XodimlarDetail, name='xodimlar-detail'),

    path('markazlar_bolimlar/', MarkazlarBolimlarListCreate.as_view(), name='markazlar-bolimlar-list-create'),
    path('markazlar_bolimlar/<int:pk>/', MarkazlarBolimlarDetail, name='markazlar-bolimlar-detail'),
]
