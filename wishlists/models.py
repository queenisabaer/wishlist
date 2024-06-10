from django.db import models
from django.contrib.auth.models import User
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

# Create your models here.

class WishList(models.Model):
    """
    Model representing a Wish List
    """
    wish_list_id = models.CharField(max_length=255, default= random_string, editable=False, unique=True)
    list_name = models.CharField(max_length=255, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # How to base a field on another field by overwriting the save method, was found in an article in medium
    def save(self, *args, **kwargs):
        if not self.list_name:
            self.list_name = self.wish_list_id
        super().save(*args, **kwargs)


