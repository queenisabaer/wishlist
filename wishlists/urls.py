from . import views
from django.urls import path
from .views import AddWishList, WishListOverview, WishListDetail


urlpatterns = [
    path('add_wish_list', AddWishList.as_view(), name='add_wishlist'),
    path('wishlist_list', WishListOverview.as_view(), name='wishlist_list'),
    path('<slug:wish_list_id>/', WishListDetail.as_view(), name ='wishlist_detail'),
]
