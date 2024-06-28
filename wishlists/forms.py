from django import forms
from django.core.exceptions import ValidationError
from .models import WishList, Item
from datetime import date, timedelta


class WishListForm(forms.ModelForm):
    """
    Form to create a new wish list.

    Attributes:
        due_date (DateField): The due date of the wish list.
        list_name (CharField): The name of the wish list.
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

    def clean_due_date(self):
        """
        Validates that the due_date is not in the past.

        Raises:
            ValidationError: If the due date is today or in the past.

        Returns:
            date: The validated due date.
        """
        due_date = self.cleaned_data.get("due_date")
        if due_date is not None:
            if due_date <= date.today():
                raise ValidationError(
                    "The due date must be at least one day in the future."
                )
        return due_date


class ItemForm(forms.ModelForm):
    """
    Form to add an item to the wishlist.

    Attributes:
        item_name (CharField): The name of the item.
        item_link (URLField): The URL link to the item.
        price (DecimalField): The price of the item.
        quantity (IntegerField): The quantity of the item.
        priority (IntegerField): The priority level of the item.
        image (ResizedImageField): The image of the item.
        image_alt (CharField): The alt text for the image.
    """
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
            "item_link": "Purchase link",
            "price": "Price (approx.)",
            "quantity": "How many do you wish for?",
            "priority": "Priority of this wish",
            "image": "Image (Default image will be provided)",
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
        if price > 1000:
            raise forms.ValidationError(
                "Please be kind to your loved ones. "
                "The price must be less than or equal to 1000."
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
            raise forms.ValidationError(
                "The quantity must be greater than zero.")
        if quantity > 100:
            raise forms.ValidationError(
                "Please be kind to your loved ones. 100 Should be enough."
            )
        return quantity
