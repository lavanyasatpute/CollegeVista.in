from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class authenticate(UserCreationForm):
    name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    #password = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password','password2','name']
    def save(self, commit=True):
        user = super(authenticate,self).save(commit=False)
        user.name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user        


