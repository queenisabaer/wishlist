from django import forms 
from django.contrib.auth.models import User
from .models import UserProfile 


class EditProfileForm(forms.ModelForm):

    username = forms.CharField(max_length=50, required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name',]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(EditProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username
            self.fields['email'].initial = user.email

    def save(self, commit=True):
        user_profile = super(EditProfileForm, self).save(commit=False)
        user = user_profile.user
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user_profile.save()
        return user_profile