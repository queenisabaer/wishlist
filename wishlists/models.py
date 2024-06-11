from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_resized import ResizedImageField
import random
import string

# Helper function

def random_string(length=10):
    '''
    Generate a random string with letters and numbers
    '''
    letters = string.ascii_letters
    numbers = string.digits
    random_str = ''.join((random.choice(letters + numbers)) for i in range(length))
    return random_str


PRIORITY = ((0, "high"), (1, "medium"), (2, "low"), (3, "no-priority"))

class WishList(models.Model):
    """
    A model representing a Wish List
    """
    wish_list_id = models.CharField(max_length=255, default= random_string, editable=False, unique=True)
    list_name = models.CharField(max_length=255, blank=False)
    due_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name= 'wish_list_owner'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on", "created_by", "list_name"]

    def __str__(self):
        return str(self.list_name)
    

    # How to base a field on another field by overwriting the save method, was found in an article in medium
    def save(self, *args, **kwargs):
        if not self.list_name:
            self.list_name = self.wish_list_id
        super().save(*args, **kwargs)

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=250, blank=False, null=False)
    item_link = models.URLField(blank=True)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    quantity = models.IntegerField()
    priority = models.IntegerField(choices=PRIORITY, default=3)
    wish_list = models.ForeignKey(
        WishList, on_delete=models.CASCADE, blank=True, null=True, 
        related_name="wishlist_item"
        )
    # To create, store & use images in models, used a tutorial by Daisy Mc Girr
    image = ResizedImageField(
        size=[200, None], quality=100, upload_to='items/', force_format='WEBP',
        blank=False, null=False, default="items/placeholder_item.webp"
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False, default="item image")


    class Meta:
        ordering = ["priority"]

    def __str__(self):
        return str(self.item_name)