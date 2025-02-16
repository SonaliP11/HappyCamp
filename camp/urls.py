from . import views
from django.urls import path

urlpatterns = [
    path('', views.ClubList.as_view(), name='home'),
    # path('', views.index, name='home'),
    path('club/<slug:slug>/', views.club_detail, name='club_detail'),
]