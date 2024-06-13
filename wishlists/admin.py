from django.contrib import admin
from .models import WishList, Item
from django_summernote.admin import SummernoteModelAdmin


@admin.register(WishList)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('list_name', 'due_date', 'created_by', 'occassion', 'wish_list_id')
    search_fields = ['list_name', 'created_by', 'occassion' ]
    list_filter = ('occassion', 'created_by')
    summernote_fields = ('description',)

# Register your models here.
admin.site.register(Item)