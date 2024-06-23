from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile


# def profile_page(request):
  #  """
   # View to render the profile page.

    #Args:
     #   request (HttpRequest): The HTTP request object.

    #Returns:
     #   HttpResponse: The rendered profile page.
    #"""
    #return redirect("/wishlists/wishlist_list")

@login_required
def profile_page(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render (request, 'profilemanagement/profile.html', {'user_profile': user_profile})