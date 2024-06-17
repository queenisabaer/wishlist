from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import WishList
from .forms import WishListForm
from django.contrib.auth. mixins import LoginRequiredMixin


class WishListOverview(generic.ListView):
    model = WishList
    template_name = "wishlists/wishlist_list.html"
    context_object_name = "wishlists"

class AddWishList(LoginRequiredMixin, generic.CreateView):
    """ Add a new Wish List view """
    template_name = 'wishlists/add_wishlist.html'
    model = WishList
    form_class = WishListForm
    success_url = '/'

    def form_valid(self, form):
        'Update instance of user'
        form.instance.created_by = self.request.user
        messages.success(self.request, "Your wish list has been created and can be seen in your profile")
        return super(AddWishList, self).form_valid(form)
    

class WishListDetail(generic.DetailView):
    """ View a single wish list """
    model = WishList
    template_name = "wishlists/wishlist_detail.html"
    context_object_name = 'wishlist'
    slug_field = 'wish_list_id'  
    slug_url_kwarg = 'wish_list_id' 