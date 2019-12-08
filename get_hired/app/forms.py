from django import forms
from .models import User


class SignUpForm(forms.ModelForm):
    Username = forms.CharField(max_length=255)
    Email = forms.EmailField(max_length=255)
    Password = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('Username', "Email", "Password",)
