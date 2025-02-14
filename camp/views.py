from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Club

# Create your views here.

class ClubList(generic.ListView):
    model = Club
    queryset = Club.objects.all()
    template_name = "camp/index.html"

def club_detail(request, slug):
    club = get_object_or_404(Club, slug=slug)
    return render(request, 'camp/club_detail.html', {'club': club})
