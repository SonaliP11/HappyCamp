from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Club
# from django.views import generic
from datetime import datetime, timedelta

# Create your views here.


# class ClubList(generic.ListView):
#     model = Club
#     queryset = Club.objects.all()
#     template_name = "camp/index.html"

#     def get_queryset(self):
#         clubs = Club.objects.all()
#         for club in clubs:
#             club.available_spots = club.capacity - club.bookings.count()
#             club.available_percentage = (club.available_spots / club.capacity) * 100
#         return clubs

def club_detail(request, slug):
    club = get_object_or_404(Club, slug=slug)
    return render(request, 'camp/club_detail.html', {'club': club})

def index(request):
    today = timezone.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    print(start_of_week)
    end_of_week = start_of_week + timedelta(days=6)
    print(end_of_week)
    start_of_next_week = end_of_week + timedelta(days=1)
    print(start_of_next_week)
    end_of_next_week = start_of_next_week + timedelta(days=6)
    print(end_of_next_week)

    this_week_clubs = Club.objects.filter(start_date__range=[start_of_week, end_of_week])
    print(this_week_clubs)
    next_week_clubs = Club.objects.filter(start_date__range=[start_of_next_week, end_of_next_week])

    context = {
        'this_week_clubs': this_week_clubs,
        'next_week_clubs': next_week_clubs,
    }
    return render(request, 'camp/index.html', context)
