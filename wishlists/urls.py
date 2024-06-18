from django.urls import path, include
from .views import AddWishList, WishListOverview, WishListDetail, DeleteWishList, EditWishList


urlpatterns = [
    path('add_wish_list', AddWishList.as_view(), name='add_wishlist'),
    path('wishlist_list', WishListOverview.as_view(), name='wishlist_list'),
    path('<slug:wish_list_id>/', WishListDetail.as_view(), name ='wishlist_detail'),
    path('delete/<slug:wish_list_id>/', DeleteWishList.as_view(), name ='delete_wishlist'),
    path('edit/<slug:wish_list_id>/', EditWishList.as_view(), name ='edit_wishlist'),
]
