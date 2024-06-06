from django.shortcuts import render

# Create your views here.


def home_page(request):
    '''
    Display home page to start a new wishlist, login or signup
    '''
    return render(request, 'home/index.html')