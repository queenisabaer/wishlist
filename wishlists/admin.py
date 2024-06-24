from django.contrib import admin
from .models import WishList, Item
from django_summernote.admin import SummernoteModelAdmin


@admin.register(WishList)
class WishListAdmin(SummernoteModelAdmin):
    list_display = ("list_name", "due_date", "created_by",
                    "occassion", "wish_list_id")
    search_fields = ["list_name"]
    list_filter = ("occassion", "created_by")
    summernote_fields = ("description",)


@admin.register(Item)
class ItemAdmin(SummernoteModelAdmin):
    list_display = ("item_name", "wish_list", "price", "quantity", "priority")
    search_fields = ["item_name"]
    list_filter = ("wish_list", "priority")
