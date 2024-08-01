from django.urls import path

from markazlar_va_bolimlar.views import Markazlar_bolimlarListView, markazlar_bolimlardetail, Bolimlar_tarixListView, \
    bolimlar_tarixdetail, AzolarListView, azolardetail, RasmListView, rasmdetail

urlpatterns = [
    path('markazlar-bolimlar/', Markazlar_bolimlarListView.as_view(), name='markazlar_bolimlar-list'),
    path('markazlar-bolimlar/<int:pk>/', markazlar_bolimlardetail, name='markazlar_bolimlar-detail'),

    path('bolimlar-tarix/', Bolimlar_tarixListView.as_view(), name='bolimlar_tarix-list'),
    path('bolimlar-tarix/<int:pk>/', bolimlar_tarixdetail, name='bolimlar_tarix-detail'),

    # path('tadqiqot/', TadqiqotListView.as_view(), name='tadqiqot-list'),
    # path('tadqiqot/<int:pk>/', tadqiqotdetail, name='tadqiqot-detail'),

    path('azolar/', AzolarListView.as_view(), name='azolar-list'),
    path('azolar/<int:pk>/', azolardetail, name='azolar-detail'),

    path('rasm/', RasmListView.as_view(), name='rasm-list'),
    path('rasm/<int:pk>/', rasmdetail, name='rasm-detail'),

#     path('video/', VideoListView.as_view(), name='video-list'),
#     path('video/<int:pk>/', videodetail, name='video-detail'),
 ]