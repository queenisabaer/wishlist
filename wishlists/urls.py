from . import views
from django.urls import path
from .views import AddWishList


urlpatterns = [
    path('add_wish_list', AddWishList.as_view(), name='add_wishlist'),
]
