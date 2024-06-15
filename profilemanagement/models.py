from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from wishlists.models import WishList

# Create your models here.

class UserProfile(models.Model):
    '''
    Model for user profile
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False, null=True)
    last_name = models.CharField(max_length=50, blank=False, null=True)
    user_mail = models.EmailField(max_length=254, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_wish_list = models.ForeignKey(WishList, on_delete=models.CASCADE)
    

