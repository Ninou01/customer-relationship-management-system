from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.db import models
from .models import Order, Customer

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'status']



class CreateUserForm(UserCreationForm):
        
    password2 = forms.CharField(
    label=_("Confirm password"),
    widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    strip=False,
    help_text=_("Enter the same password as before, for verification."),
    )
    
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        
    def clean_username(self, *args, **kwargs):
        data = self.cleaned_data.get('username')
        if User.objects.filter(username = data).exists():
            raise forms.ValidationError("user '%s' already exist "%data)
        return data

        

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'date_crated']