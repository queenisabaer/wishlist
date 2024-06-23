from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from wishlists.models import WishList

# Create your models here.


class UserProfile(models.Model):
    """
    Model representing a user profile.

    Attributes:
        user (OneToOneField): The associated User object.
        first_name (CharField): The user's first name.
        last_name (CharField): The user's last name.
        created_on (DateTimeField): Timestamp when the profile was created.
        updated_at (DateTimeField): Timestamp when the profile was last updated.
        user_wish_list (ForeignKey): The user's associated wish list.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False, null=True)
    last_name = models.CharField(max_length=50, blank=False, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_wish_list = models.ForeignKey(WishList, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


# Got this code from a tutorial by Daisy McGee
@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """
    Create a user profile when a user is created

    Parameters:
    instance (User): The User instance that was saved.
    created (bool): A boolean indicating whether a new User instance was created.
    **kwargs: Additional keyword arguments passed by the signal."""
    if created:
        UserProfile.objects.create(user=instance)
