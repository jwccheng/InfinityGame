from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='Required. Add a valid username')

    class Meta:
        model = Account
        fields = ('username','email','password1','password2')
