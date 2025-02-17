from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from .models import Club
from datetime import datetime, timedelta
def club_detail(request, slug):
    club = get_object_or_404(Club, slug=slug)
    return render(request, 'camp/club_detail.html', {'club': club})
class ClubList(generic.ListView):
    model = Club
    template_name = "camp/index.html"
    def get_queryset(self):
        today = timezone.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        start_of_next_week = end_of_week + timedelta(days=1)
        end_of_next_week = start_of_next_week + timedelta(days=6)
        this_week_clubs = Club.objects.filter(start_date__range=[start_of_week, end_of_week]).order_by('start_date')
        next_week_clubs = Club.objects.filter(start_date__range=[start_of_next_week, end_of_next_week]).order_by('start_date')
        for club in this_week_clubs:
            club.available_spots = club.capacity - club.bookings.count()
            club.available_percentage = (club.available_spots / club.capacity) * 100 if club.capacity > 0 else 0
        for club in next_week_clubs:
            club.available_spots = club.capacity - club.bookings.count()
            club.available_percentage = (club.available_spots / club.capacity) * 100 if club.capacity > 0 else 0
        return {
            'this_week_clubs': this_week_clubs,
            'next_week_clubs': next_week_clubs,
        }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_queryset())
        context['now'] = timezone.now()
        return context