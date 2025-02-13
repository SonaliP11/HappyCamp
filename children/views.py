from django.shortcuts import render
from .models import Child
from django.views import generic

# Create your views here.
class ChildList(generic.ListView):
    model = Child

