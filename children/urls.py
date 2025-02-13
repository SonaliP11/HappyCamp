from django.urls import path
from .views import child_list, child_detail, child_create, child_update, child_delete

urlpatterns = [
    path('', child_list, name='child-list'),  # List all children
    path('<int:child_id>/', child_detail, name='child-detail'),  # Child details
    path('add/', child_create, name='child-create'),  # Add child
    path('<int:child_id>/edit/', child_update, name='child-update'),  # Edit child
    path('<int:child_id>/delete/', child_delete, name='child-delete'),  # Delete child
]