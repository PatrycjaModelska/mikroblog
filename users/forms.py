from django import forms
from users.models import Users

from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = Users
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ("first_name", "last_name", "username", "email")


class EditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = Users
        fields = ("first_name", "last_name", "email")


class PassForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ("password",)
