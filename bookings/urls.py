from django.urls import path
from .views import booking_list, booking_create, booking_cancel

urlpatterns = [
    path('', booking_list, name='booking-list'),  # View all bookings
    path('add/', booking_create, name='booking-create'),  # Create a new booking
    path('<int:booking_id>/cancel/', booking_cancel, name='booking-cancel'),  # Cancel a booking
]