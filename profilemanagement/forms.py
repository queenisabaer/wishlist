from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class EditProfileForm(forms.ModelForm):
    """
    A form for editing the user's profile.

    This form allows users to edit their profile information including their
    username, first name, last name, and email. It initializes the username and
    email fields with the current values from the User instance.

    Attributes:
        username (CharField): The user's username, required with a max length
        of 50.
        first_name (CharField): The user's first name, optional with a max
        length of 50.
        last_name (CharField): The user's last name, optional with a max
        length of 50.
        email (EmailField): The user's email, required.

    Meta:
        model (UserProfile): The model associated with this form.
        fields (list): The fields to be included in the form, specifically
        first_name and last_name.

    Methods:
        __init__(*args, **kwargs):
            Initializes the form, optionally populating initial values for
            username and email from the given user.
        save(commit=True):
            Saves the updated user profile and user information.
    """
    username = forms.CharField(max_length=50, required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = [
            "first_name",
            "last_name",
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(EditProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields["username"].initial = user.username
            self.fields["email"].initial = user.email

    def save(self, commit=True):
        user_profile = super(EditProfileForm, self).save(commit=False)
        user = user_profile.user
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            user_profile.save()
        return user_profile
