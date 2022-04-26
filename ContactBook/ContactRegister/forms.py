from django import forms
from django.forms import ModelForm
from .models import*




class ContactregisterForm(forms.ModelForm):
# Meta - Class about class ie; Data about data

    class Meta:
        model=contactregister

        fields="__all__" # All fields Display
        
        #fields=['name',] # Selected fields will display

