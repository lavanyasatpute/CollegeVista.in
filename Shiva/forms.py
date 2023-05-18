from django import forms
from .models import Contact


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','username', 'email', 'password','conformpassword']