from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page(request):
    '''
    Display home page to start a new wishlist, login or signup
    '''
    return HttpResponse("Hello World!")
    #return render(request, 'home/index.html', )