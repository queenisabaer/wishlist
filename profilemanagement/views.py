from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import EditProfileForm

# def profile_page(request):
#  """
# View to render the profile page.

# Args:
#   request (HttpRequest): The HTTP request object.

# Returns:
#   HttpResponse: The rendered profile page.
# """
# return redirect("/wishlists/wishlist_list")


@login_required
def profile_page(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(
        request,
        "profilemanagement/profile.html",
        {"user_profile": user_profile}
    )


@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        form = EditProfileForm(
            data=request.POST, instance=user_profile, user=request.user
        )
        if form.is_valid():
            messages.success(request,
                             "Your profile has been successfully updated")
            form.save()
            return redirect("profile")
        else:
            messages.error(
                "Something is missing. Please check if you added all relevant "
                "information"
            )
    else:
        form = EditProfileForm(instance=user_profile, user=request.user)

    return render(request,
                  "profilemanagement/edit_profile.html",
                  {"form": form})


@login_required
def delete_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        profile.user.delete()
        messages.success(request, "Your profile has been deleted.")
        return redirect("home")
    else:
        return render(request, "profilemanagement/delete_profile.html")
