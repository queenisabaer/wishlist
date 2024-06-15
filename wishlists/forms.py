from django import forms 
from .models import WishList


class WishListForm(forms.ModelForm):
    """ 
    Form to create a new wish list
    """
    due_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    list_name = forms.CharField(max_length=255, initial='')

    class Meta:
        model = WishList
        fields = ['list_name', 'due_date', 'description', 'occassion']
        labels = {
            'list_name': 'Wish List Name',
            'due_date': 'Due Date',
            'description': 'Description',
            'occassion': 'Occassion'
        }


        
