from . import views
from django.urls import path
from .views import AddWishList, WishListOverview


urlpatterns = [
    path('add_wish_list', AddWishList.as_view(), name='add_wishlist'),
    path('wishlist_list', WishListOverview.as_view(), name='wishlist_list')
]
