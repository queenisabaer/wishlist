from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from wishlists.models import WishList

# Create your models here.

class UserProfile(models.Model):
    """
    Model representing a user profile.

    Attributes:
        user (OneToOneField): The associated User object.
        first_name (CharField): The user's first name.
        last_name (CharField): The user's last name.
        user_mail (EmailField): The user's email address.
        created_on (DateTimeField): Timestamp when the profile was created.
        updated_at (DateTimeField): Timestamp when the profile was last updated.
        user_wish_list (ForeignKey): The user's associated wish list.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False, null=True)
    last_name = models.CharField(max_length=50, blank=False, null=True)
    user_mail = models.EmailField(max_length=254, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_wish_list = models.ForeignKey(WishList, on_delete=models.CASCADE)
    

