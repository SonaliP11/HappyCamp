from django.shortcuts import render
from django.views import generic
from .models import Club

# Create your views here.

class ClubList(generic.ListView):
    model = Club
    queryset = Club.objects.all()
    template_name = "camp/index.html"
