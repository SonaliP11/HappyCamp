from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Club
from datetime import datetime, timedelta

# Create your views here.

def club_detail(request, slug):
    club = get_object_or_404(Club, slug=slug)
    return render(request, 'camp/club_detail.html', {'club': club})

def index(request):
    today = timezone.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    start_of_next_week = end_of_week + timedelta(days=1)
    end_of_next_week = start_of_next_week + timedelta(days=6)

    this_week_clubs = Club.objects.filter(start_date__range=[start_of_week, end_of_week])
    next_week_clubs = Club.objects.filter(start_date__range=[start_of_next_week, end_of_next_week])

    clubs = Club.objects.all()
    for club in clubs:
        club.available_spots = club.capacity - club.bookings.count()
        club.available_percentage = (club.available_spots / club.capacity) * 100

    context = {
        'this_week_clubs': this_week_clubs,
        'next_week_clubs': next_week_clubs,
        'clubs': clubs,
    }
    return render(request, 'camp/index.html', context)
