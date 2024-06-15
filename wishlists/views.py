from django.shortcuts import render
from django.views import generic
from .models import WishList
from .forms import WishListForm
from django.contrib.auth. mixins import LoginRequiredMixin


class WishListOverview(generic.ListView):
    model = WishList

class AddWishList(LoginRequiredMixin, generic.CreateView):
    """ Add Wishlist view """
    template_name = 'wishlists/add_wishlist.html'
    model = WishList
    form_class = WishListForm
    success_url = ''

    def form_valid(self, form):
        'Update instance of user'
        form.instance.created_by = self.request.user
        return super(AddWishList, self).form_valid(form)
    