from django import forms
from django.contrib.auth.models import User



class authenticate(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        


