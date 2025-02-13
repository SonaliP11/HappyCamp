from . import views
from django.urls import path

urlpatterns = [
    path('', views.ChildList.as_view(), name='child-list'),
]