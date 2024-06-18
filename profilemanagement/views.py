from django.shortcuts import redirect

def profile_page(request):
    """
    View to render the profile page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered profile page.
    """
    return redirect('/wishlists/wishlist_list')