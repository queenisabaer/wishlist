from django.shortcuts import render

# Create your views here.


def home_page(request):
    """
    View to render the index.html template, which allows users to start a
    new wish list, log in, or sign up.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, "home/index.html")
