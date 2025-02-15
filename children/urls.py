from django.urls import path
from . import views

urlpatterns = [
    path('', views.child_list, name='child-list'),
    path('add/', views.child_create, name='child-create'),
    ## path('<int:child_id>/', views.child_detail, name='child-detail'),
    path('<int:child_id>/edit/', views.child_update, name='child-update'),
    path('<int:child_id>/delete/', views.child_delete, name='child-delete'),
]