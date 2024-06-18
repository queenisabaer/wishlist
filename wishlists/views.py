from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.views import generic
from .models import WishList
from .forms import WishListForm


class WishListOverview(generic.ListView):
    """ View for displaying an overview of all wish lists. """
    model = WishList
    template_name = "wishlists/wishlist_list.html"
    context_object_name = "wishlists"

class AddWishList(LoginRequiredMixin, generic.CreateView):
    """ View for adding a new wish list. Requires the user to be logged in. """
    template_name = 'wishlists/add_wishlist.html'
    model = WishList
    form_class = WishListForm
    success_url = '/'

    def form_valid(self, form):
        """
        Set the created_by field to the current user and display a success message.

        Args:
            form: The form instance being validated.

        Returns:
            HttpResponse: The HTTP response for a valid form.
        """
        form.instance.created_by = self.request.user
        messages.success(self.request, "Your wish list has been created and can be seen in your profile")
        return super(AddWishList, self).form_valid(form)
    

class WishListDetail(generic.DetailView):
    """ View for displaying details of a single wish list. """
    model = WishList
    template_name = "wishlists/wishlist_detail.html"
    context_object_name = 'wishlist'
    slug_field = 'wish_list_id'  
    slug_url_kwarg = 'wish_list_id'


class DeleteWishList(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """ View for deleting a wish list. Requires the user to be logged in and to be the creator of the wish list. """
    model = WishList
    template_name = 'wishlists/delete_wish_list.html'
    success_url = '/wishlists/wishlist_list'
    slug_field = 'wish_list_id'  
    slug_url_kwarg = 'wish_list_id'

    def test_func(self):
        """
        Check if the current user is the creator of the wish list.

        Returns:
            bool: True if the user is the creator, False otherwise.
        """
        return self.request.user == self.get_object().created_by
    
    def handle_no_permission(self):
        """
        Handle the case where the user does not have permission to delete the wish list.

        Returns:
            HttpResponse: The response for a user without permission.
        """
        if not self.request.user.is_authenticated:
            messages.info(self.request, "You need to log in first to delete a wish list.")
            return redirect('account_login') 
        return super().handle_no_permission()

    def delete(self, request,  *args, **kwargs):
        """
        Delete the wish list and display a success message.

        Args:
            request: The HTTP request.

        Returns:
            HttpResponse: The HTTP response after the wish list is deleted.
        """
        messages.success(self.request, "Your wish list has been deleted")
        return super(DeleteWishList, self).delete(request, *args, **kwargs)