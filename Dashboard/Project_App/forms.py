from django.forms import fields
from .models import User
from django import forms 


class UserForms(forms.Form):
    class Meta:
        model = User
        fields = ['first_name','last_name','username']
