from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
import datetime
from account.models import Account, bankType
from mptt.forms import TreeNodeChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple
from django_select2.forms import Select2MultipleWidget, ModelSelect2Widget
from django.forms.widgets import SelectDateWidget
from django.core.validators import MinValueValidator, MaxValueValidator


luckyNumberType = [
    ("FRONT", "FRONT"),
    ("BACK", "BACK"),
]

RubyRegister = [
    ("100", "100"),
    ("200", "200"),
    ("300", "300"),
    ("400", "400"),
    ("500", "500"),
    ("600", "600"),
    ("700", "700"),
    ("800", "800"),
    ("900", "900"),
    ("1000", "1000"),
]

class NewUserForm(UserCreationForm):
    username = forms.CharField(max_length=12, min_length=5)
    class Meta:
        model = Account
        fields = ("username", "password1", "password2", "user_mobile")

class MemberUserForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    username = forms.CharField(max_length=12, min_length=5)
    class Meta:
        model = Account
        fields = ("username", "email", "user_mobile", "password1", "password2")

class Point(forms.Form):
    amount = forms.ChoiceField(choices=RubyRegister)

class FrontLuckyNumber(forms.Form):
    num1 = forms.IntegerField(min_value=1, max_value=7)
    num2 = forms.IntegerField(min_value=0, max_value=9)
    num3 = forms.IntegerField(min_value=0, max_value=9)
    num4 = forms.IntegerField(min_value=0, max_value=9)
    quantity = forms.IntegerField(min_value=1)

class BackLuckyNumber(forms.Form):
    num1 = forms.IntegerField(min_value=0, max_value=9)
    num2 = forms.IntegerField(min_value=0, max_value=9)
    num3 = forms.IntegerField(min_value=0, max_value=9)
    num4 = forms.IntegerField(min_value=0, max_value=9)
    quantity = forms.IntegerField(min_value=1)

class EditProfile(forms.Form):
    user_mobile = forms.CharField(max_length=12)

class Convert(forms.Form):
    amount = forms.DecimalField()

class TopUp(forms.Form):
    amount = forms.DecimalField()