from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']
