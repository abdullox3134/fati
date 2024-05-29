from django.urls import path

from doktarantura.views import Qabul_tartibiListView, qabul_tartibidetail, Malakaviy_imtihonListView, \
    malakaviy_imtihondetail, DoktaranturaListView, doktaranturadetail

urlpatterns = [
    path('qabul-tartibi/', Qabul_tartibiListView.as_view()),
    path('qabul-tartibi/<int:pk>/', qabul_tartibidetail),

    path('malakaviy-imtihon/', Malakaviy_imtihonListView.as_view()),
    path('malakaviy-imtihon/<int:pk>', malakaviy_imtihondetail),

    path('doktarantura/', DoktaranturaListView.as_view()),
    path('doktarantura/<int:pk>/', doktaranturadetail),
]