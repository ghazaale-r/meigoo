# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import (Customer, 
                     RestaurantManager)

from restaurant.models import ( 
                     Restaurant, Address )


class CustomerSignUpForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['email', 'password1', 'password2']


class ManagerSignUpForm(UserCreationForm):
    restaurant_name = forms.CharField(max_length=255)
    street = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=50)
    zipcode = forms.CharField(max_length=10, required=False)
    categories = forms.MultipleChoiceField(choices=[]) 
    
    def __init__(self, *args, **kwargs):
        super(ManagerSignUpForm, self).__init__(*args, **kwargs)
        from restaurant.models import Category 
        self.fields['categories'].choices = [(cat.id, cat.name) for cat in Category.objects.all()]

    
    class Meta:
        model = RestaurantManager
        fields = ['email', 'password1', 'password2']
