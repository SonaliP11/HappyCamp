from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm
from camp.models import Club

# List all bookings for the logged-in parent
@login_required
def booking_list(request):
    bookings = Booking.objects.filter(parent=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})
# Create a new booking
@login_required
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.parent = request.user
            booking.save()
            return redirect('booking-list')
    else:
        form = BookingForm(user=request.user)
    return render(request, 'bookings/booking_form.html', {'form': form})
# Cancel a booking
@login_required
def booking_cancel(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, parent=request.user)
    if request.method == 'POST':
        booking.status = 'cancelled'
        booking.save()
        return redirect('booking-list')
    return render(request, 'bookings/booking_confirm_cancel.html', {'booking': booking})
