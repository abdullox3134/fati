from django.urls import path
from xalqaro_aloqalar.views import (Xamkor_tashkilotListView, xamkor_tashkilotdetail, Xamkor_loihalarListView,\
      xamkor_loihalardetail, Xalqaro_sayohatlarListView, xalqaro_sayohatlardetail, TadqiqotListView, Tadqiqotdetail,
                                    KelganlarListView, Kelganlardetail)


urlpatterns = [
    path('xamkor-tashkilot/', Xamkor_tashkilotListView.as_view(), name='xamkor_tashkilot-list'),
    path('xamkor-tashkilot/<int:pk>/', xamkor_tashkilotdetail, name='xamkor_tashkilot-detail'),

    path('xamkor-loihalar/', Xamkor_loihalarListView.as_view(), name='xamkor_loihalar-list'),
    path('xamkor-loihalar/<int:pk>/', xamkor_loihalardetail, name='xamkor_loihalar-detail'),

    # path('xalqaro-tadqiqot/', Xalqaro_tadqiqotListView.as_view(), name='xalqaro_tadqiqot-list'),
    # path('xalqaro-tadqiqot/<int:pk>/', xalqaro_tadqiqotdetail, name='xalqaro_tadqiqot-detail'),

    path('xalqaro-sayohatlar/', Xalqaro_sayohatlarListView.as_view(), name='xalqaro_sayohatlar-list'),
    path('xalqaro-sayohatlar/<int:pk>/', xalqaro_sayohatlardetail, name='xalqaro_sayohatlar-detail'),

    path('tadqiqot/', TadqiqotListView.as_view(), name='tadqiqot-list'),
    path('tadqiqot/<int:pk>/', Tadqiqotdetail, name='tadqiqot-detail'),

    path('Kelganlar/', KelganlarListView.as_view(), name='Kelganlar-list'),
    path('Kelganlar/<int:pk>/', Kelganlardetail, name='Kelganlar-detail'),

]
