from . import views
from django.urls import path

urlpatterns = [
    path('', views.WishListOverview.as_view(), name="wishlists")
]
