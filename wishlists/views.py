from django.shortcuts import render
from django.views import generic
from .models import WishList

class WishListOverview(generic.ListView):
    model = WishList
