from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Mete(UserCreationForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields + "age"


class CustomUserChangeForm(UserCreationForm):

    class Mete(UserCreationForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields
