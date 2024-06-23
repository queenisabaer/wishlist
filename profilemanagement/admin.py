from django.contrib import admin
from .models import UserProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(UserProfile)
class WishListAdmin(SummernoteModelAdmin):
    list_display = ('pk', 'user', 'first_name', 'last_name')
    search_fields = ['last_name']