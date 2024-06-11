from django.contrib import admin
from .models import WishList, Item

# Register your models here.
admin.site.register(WishList)
admin.site.register(Item)