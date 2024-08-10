from django.urls import path
#
# from kengashlar.views import Institut_ken_azolariListView, institut_ken_azolaridetail, Ilmiy_kengash_majlisListView, \
#     ilmiy_kengash_majlisdetail, Qabul_korib_gan_dissertatsiyaListView, qabul_korib_gan_dissertatsiyadetail, \
#     Shifr_va_passportListView, shifr_va_passportdetail, Dissertatsiya_va_avtorefListView, \
#     dissertatsiya_va_avtorefdetail, Dissertatsiya_fayllarListView, dissertatsiya_fayllardetail, Yosh_olimlarListView, \
#     yosh_olimlardetail, Yosh_olimlar_azolariListView, yosh_olimlar_azolaridetail, MaruzalarListView, maruzalardetail
#

#     path('qabul-korib-gan-dissertatsiya/', Qabul_korib_gan_dissertatsiyaListView.as_view(),
#          name='qabul_korib_gan_dissertatsiya-list'),
#     path('qabul-korib-gan-dissertatsiya/<int:pk>/', qabul_korib_gan_dissertatsiyadetail,
#          name='qabul_korib_gan_dissertatsiya-detail'),
#
#     path('shifr-va-passport/', Shifr_va_passportListView.as_view(), name='shifr_va_passport-list'),
#     path('shifr-va-passport/<int:pk>/', shifr_va_passportdetail, name='shifr_va_passport-detail'),
#
#     path('dissertatsiya-va-avtoref/', Dissertatsiya_va_avtorefListView.as_view(), name='dissertatsiya_va_avtoref-list'),
#     path('dissertatsiya-va-avtoref/<int:pk>/', dissertatsiya_va_avtorefdetail, name='dissertatsiya_va_avtoref-detail'),
#
#     path('dissertatsiya-fayllar/', Dissertatsiya_fayllarListView.as_view(), name='dissertatsiya_fayllar-list'),
#     path('dissertatsiya-fayllar/<int:pk>/', dissertatsiya_fayllardetail, name='dissertatsiya_fayllar-detail'),
#
#     path('yosh-olimlar/', Yosh_olimlarListView.as_view(), name='yosh_olimlar-list'),
#     path('yosh-olimlar/<int:pk>/', yosh_olimlardetail, name='yosh_olimlar-detail'),
#
#     path('yosh-olimlar-azolari/', Yosh_olimlar_azolariListView.as_view(), name='yosh_olimlar_azolari-list'),
#     path('yosh-olimlar-azolari/<int:pk>/', yosh_olimlar_azolaridetail, name='yosh_olimlar_azolari-detail'),
#
#     path('maruzalar/', MaruzalarListView.as_view(), name='maruzalar-list'),
#     path('maruzalar/<int:pk>/', maruzalardetail, name='maruzalar-detail'),
# ]
from .views import (AzolarListView, Azolardetail, DissertatsiyaIshlarListView, DissertatsiyaIshlardetail,
                    ContentListView, Contentdetail)

urlpatterns = [
    path('institut-ken-azolari/', AzolarListView.as_view(), name='institut_ken_azolari-list'),
    path('institut-ken-azolari/<int:pk>/', Azolardetail, name='institut_ken_azolari-detail'),

    path('DissertatsiyaIshlar/', DissertatsiyaIshlarListView.as_view(), name='DissertatsiyaIshlar-list'),
    path('DissertatsiyaIshlar/<int:pk>/', DissertatsiyaIshlardetail, name='DissertatsiyaIshlar-detail'),

    path('Content/', ContentListView.as_view(), name='Content-list'),
    path('Content/<int:pk>/', Contentdetail, name='Content-detail'),
]