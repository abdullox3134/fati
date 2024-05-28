from django.urls import path

from seminar.views import Seminar_turlariListView, seminar_turlaridetail, SeminarListView, seminardetail, \
    Seminar_majlislariListView, seminar_majlislaridetail

urlpatterns = [
    path('seminar-turlari/', Seminar_turlariListView.as_view(), name='seminar_turlari-list'),
    path('seminar-turlari/<int:pk>/', seminar_turlaridetail, name='seminar_turlari-detail'),

    path('seminar/', SeminarListView.as_view(), name='seminar-list'),
    path('seminar/<int:pk>/', seminardetail, name='seminar-detail'),

    path('seminar-majlislari/', Seminar_majlislariListView.as_view(), name='seminar_majlislari-list'),
    path('seminar-majlislari/<int:pk>/', seminar_majlislaridetail, name='seminar_majlislari-detail'),
]