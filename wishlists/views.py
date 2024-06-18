from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.views import generic
from .models import WishList
from .forms import WishListForm
from django.contrib.auth.decorators import login_required


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


class DeleteWishList(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """ Delete a wish list """
    model = WishList
    template_name = 'wishlists/delete_wish_list.html'
    success_url = '/wishlists/wishlist_list'
    slug_field = 'wish_list_id'  
    slug_url_kwarg = 'wish_list_id'

    def test_func(self):
        return self.request.user == self.get_object().created_by
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.info(self.request, "You need to log in first to delete a wish list.")
            return redirect('account_login') 
        return super().handle_no_permission()

    def delete(self, request,  *args, **kwargs):
        messages.success(self.request, "Your wish list has been deleted")
        return super(DeleteWishList, self).delete(request, *args, **kwargs)