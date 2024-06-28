from django.contrib import admin
from .models import UserProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(UserProfile)
class WishListAdmin(SummernoteModelAdmin):
    """
    Admin interface options for the UserProfile model.

    This class customizes the admin interface for the UserProfile model,
    providing enhanced functionality such as customized list display and search
    fields.

    Attributes:
        list_display (tuple): Fields to be displayed in the list view of the
        admin interface.
        search_fields (list): Fields that can be searched in the admin
        interface.
    """
    list_display = ("pk", "user", "first_name", "last_name")
    search_fields = ["last_name"]
