from django import forms
from .models import WishList, Item


class WishListForm(forms.ModelForm):
    """
    Form to create a new wish list
    """

    due_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    list_name = forms.CharField(max_length=255, initial="")

    class Meta:
        model = WishList
        fields = ["list_name", "due_date", "description", "occassion"]
        labels = {
            "list_name": "Wish List Name",
            "due_date": "Due Date",
            "description": "Description",
            "occassion": "Occassion",
        }


class ItemForm(forms.ModelForm):
    """Form to add an item to the wishlist"""

    class Meta:
        model = Item
        fields = [
            "item_name",
            "item_link",
            "price",
            "quantity",
            "priority",
            "image",
            "image_alt",
        ]
        labels = {
            "item_name": "Item Name",
            "item_link": "Link",
            "price": "Price",
            "quantity": "Quantity",
            "priority": "Priority",
            "image": "Image",
            "image_alt": "Image Description(for screen readers)",
        }

    def clean_price(self):
        """
        Ensure that the price is greater than or equal to zero.

        Raises:
            ValidationError: If the price is less than zero.

        Returns:
            Decimal: The cleaned price.
        """
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise forms.ValidationError(
                "The price must be greater than or equal to zero."
            )
        return price

    def clean_quantity(self):
        """
        Ensure that the quantity is greater than zero.

        Raises:
            ValidationError: If the quantity is less than or equal to zero.

        Returns:
            int: The cleaned quantity.
        """
        quantity = self.cleaned_data.get("quantity")
        if quantity is not None and quantity <= 0:
            raise forms.ValidationError("The quantity must be greater than zero.")
        return quantity
