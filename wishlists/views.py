from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import WishList, Item
from .forms import WishListForm, ItemForm


class WishListOverview(generic.ListView):
    """
    View for displaying an overview of all wish lists.

    This view provides a list of wish lists created by the currently
    authenticated user, rendered using the specified template.

    Attributes:
        model (Model): The model to be used for this view (WishList).
        template_name (str): The template to render the list view.
        context_object_name (str): The name of the context object to be used
        in the template.
    """
    model = WishList
    template_name = "wishlists/wishlist_list.html"
    context_object_name = "wishlists"

    def get_queryset(self):
        """
        Return wishlists created by the current user if user is
        authenticated.
        """
        if self.request.user.is_authenticated:
            return WishList.objects.filter(created_by=self.request.user)
        else:
            return WishList.objects.none()


class AddWishList(LoginRequiredMixin, generic.CreateView):
    """
    View for adding a new wish list. Requires the user to be logged in.

    This view handles the creation of a new wish list, ensuring that the
    `created_by` field is set to the current user.

    Attributes:
        template_name (str): The template to render the creation form.
        model (Model): The model to be used for this view (WishList).
        form_class (Form): The form class to be used for creating a wish list
        (WishListForm).
        success_url (str): The URL to redirect to upon successful form
        submission.
    """
    template_name = "wishlists/add_wishlist.html"
    model = WishList
    form_class = WishListForm
    success_url = reverse_lazy("wishlist_detail")

    def form_valid(self, form):
        """
        Set the created_by field to the current user and display a success
        message.

        Args:
            form: The form instance being validated.

        Returns:
            HttpResponse: The HTTP response for a valid form.
        """
        form.instance.created_by = self.request.user
        messages.success(
            self.request,
            "Your wish list has been created and can be seen in your profile",
        )
        return super(AddWishList, self).form_valid(form)

    def get_success_url(self):
        """
        Get the URL to redirect to after a successful form submission.

        Returns:
            str: The URL to redirect to.
        """
        return reverse_lazy("wishlist_detail",
                            args=[str(self.object.wish_list_id)])


class WishListDetail(generic.DetailView):
    """
    View for displaying details of a single wish list.

    This view displays the details of a specific wish list, including the items
    in the wish list and a form to add new items.

    Attributes:
        model (Model): The model to be used for this view (WishList).
        template_name (str): The template to render the detail view.
        context_object_name (str): The name of the context object to be used in
        the template.
        slug_field (str): The field used to retrieve the object by slug
        (wish_list_id).
        slug_url_kwarg (str): The URL keyword argument that contains the slug
        (wish_list_id).
    """
    model = WishList
    template_name = "wishlists/wishlist_detail.html"
    context_object_name = "wishlist"
    slug_field = "wish_list_id"
    slug_url_kwarg = "wish_list_id"

    def get_context_data(self, **kwargs):
        """
        Get the context data for rendering the template.

        This method adds the items in the wish list and an item form to the
        context.

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data for rendering the template.
        """
        context = super().get_context_data(**kwargs)
        context["items"] = Item.objects.filter(wish_list=self.object)
        if "itemForm" not in context:
            context["itemForm"] = ItemForm()
        context["form_has_errors"] = kwargs.get("form_has_errors", False)
        return context

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to add a new item to the wish list.

        This method processes the item form submission, adding the new item to
        the wish list if the form is valid.
        If the form is not valid, it re-renders the detail view with form
        errors.

        Args:
            self (WishListDetail): The instance of the WishListDetail view.
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            HttpResponse: The HTTP response for a valid or invalid form.
        """
        self.object = self.get_object()
        itemForm = ItemForm(request.POST, request.FILES)
        if itemForm.is_valid():
            item = itemForm.save(commit=False)
            item.wish_list = self.object
            item.save()
            messages.success(request, "Item has been added to your wish list.")
            return redirect("wishlist_detail",
                            wish_list_id=self.object.wish_list_id)
        else:
            context = self.get_context_data(itemForm=itemForm,
                                            form_has_errors=True)
            return self.render_to_response(context)


class EditWishList(LoginRequiredMixin, UserPassesTestMixin,
                   generic.UpdateView):
    """
    View for editing a wish list. Requires the user to be logged in and to own
    the wish list.

    Attributes:
        model (Model): The model associated with this view (WishList).
        template_name (str): The template used to render the edit form.
        success_url (str): The URL to redirect to upon successful update.
        form_class (Form): The form class to use for editing the wish list.
        slug_field (str): The field used for slug-based URL matching.
        slug_url_kwarg (str): The name of the URLConf keyword argument
                              containing the slug.
    """
    model = WishList
    template_name = "wishlists/edit_wishlist.html"
    success_url = "/wishlists/wishlist_list"
    form_class = WishListForm
    slug_field = "wish_list_id"
    slug_url_kwarg = "wish_list_id"

    def test_func(self):
        """
        Check if the current user is the creator of the wish list.

        Returns:
            bool: True if the user is the creator, False otherwise.
        """
        return self.request.user == self.get_object().created_by

    def handle_no_permission(self):
        """
        Handle the case where the user does not have permission to edit the
        wish list.

        Returns:
            HttpResponse: The response for a user without permission.
        """
        if not self.request.user.is_authenticated:
            messages.info(
                self.request, "You need to log in first to edit a wish list.")
            return redirect("account_login")
        return super().handle_no_permission()

    def form_valid(self, form):
        """
        Save the form and display a success message.

        Args:
            form: The form instance.

        Returns:
            HttpResponseRedirect: The redirect response after form processing.
        """
        messages.success(self.request, "Your wish list has been updated")
        return super().form_valid(form)


class DeleteWishList(LoginRequiredMixin, UserPassesTestMixin,
                     generic.DeleteView):
    """
    View for deleting a wish list. Requires the user to be logged in and to
    be the creator of the wish list.

    Attributes:
        model (Model): The model associated with this view (WishList).
        template_name (str): The template used to render the delete
        confirmation.
        success_url (str): The URL to redirect to upon successful deletion.
        slug_field (str): The field used for slug-based URL matching.
        slug_url_kwarg (str): The name of the URLConf keyword argument
                              containing the slug.
    """
    model = WishList
    template_name = "wishlists/delete_wish_list.html"
    success_url = "/wishlists/wishlist_list"
    slug_field = "wish_list_id"
    slug_url_kwarg = "wish_list_id"

    def test_func(self):
        """
        Check if the current user is the creator of the wish list.

        Returns:
            bool: True if the user is the creator, False otherwise.
        """
        return self.request.user == self.get_object().created_by

    def handle_no_permission(self):
        """
        Handle the case where the user does not have permission to delete the
        wish list.

        Returns:
            HttpResponse: The response for a user without permission.
        """
        if not self.request.user.is_authenticated:
            messages.info(
                self.request, "You need to log in first to delete a wish list."
            )
            return redirect("account_login")
        return super().handle_no_permission()

    def delete(self, request, *args, **kwargs):
        """
        Delete the wish list and display a success message.

        Args:
            self (DeleteWishList): The instance of the DeleteWishList view.
            request: The HTTP request.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            HttpResponse: The HTTP response after the wish list is deleted.
        """
        messages.success(self.request, "Your wish list has been deleted")
        return super(DeleteWishList, self).delete(request, *args, **kwargs)
