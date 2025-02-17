from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm
from camp.models import Club
from children.models import Child


# List all bookings for the logged-in parent
def booking_list(request):
    children = Child.objects.filter(parent=request.user) if request.user.is_authenticated else []
    bookings = Booking.objects.filter(child__in=children) if request.user.is_authenticated else []
    clubs = Club.objects.all()
    for club in clubs:
        club.available_seats = club.capacity - club.bookings.count()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings, 'clubs': clubs})
    
# Create a new booking
@login_required
def booking_create(request):
    club_id = request.GET.get('club_id')
    initial_data = {}
    if club_id:
        initial_data['club'] = get_object_or_404(Club, id=club_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.parent = request.user
            booking.save()
            messages.success(request, 'Thanks for booking, it will be confirmed soon.')
            return redirect('booking-list')
    else:
        form = BookingForm(user=request.user, initial=initial_data)
    
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


# Handle payment for a booking
@login_required
def booking_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        booking.payment_status = payment_method
        booking.save()
        return redirect('booking-list')
    return render(request, 'bookings/booking_form.html', {'booking': booking})