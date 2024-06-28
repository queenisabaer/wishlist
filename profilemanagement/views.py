from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import EditProfileForm


@login_required
def profile_page(request):
    """
    Display the user's profile page.

    This view retrieves the user's profile based on the logged-in user and
    renders the profile page template with the user's profile information.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered profile page template with user profile
        data.
    """
    user_profile = UserProfile.objects.get(user=request.user)
    return render(
        request,
        "profilemanagement/profile.html",
        {"user_profile": user_profile}
    )


@login_required
def edit_profile(request):
    """
    Display and process the edit profile form.

    This view handles both GET and POST requests to display and process the
    edit profile form. On GET request, it renders the form with the user's
    current profile data. On POST request, it validates and saves the form
    data if valid, updating the user's profile.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered edit profile form template.
        HttpResponseRedirect: Redirects to the profile page on successful
        update.
    """
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
    """
    Display and process the delete profile confirmation.

    This view handles both GET and POST requests for deleting the user's
    profile.
    On GET request, it renders the delete profile confirmation page.
    On POST request, it deletes the user's profile and redirects to the home
    page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered delete profile confirmation template.
        HttpResponseRedirect: Redirects to the home page on successful
        deletion.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        profile.user.delete()
        messages.success(request, "Your profile has been deleted.")
        return redirect("home")
    else:
        return render(request, "profilemanagement/delete_profile.html")
