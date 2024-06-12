from django.shortcuts import render
from django.http import HttpResponse

def wish_list(request):
    return HttpResponse("Hello, Wish List")
