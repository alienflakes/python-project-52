from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


class CustomUserChangeForm(CustomUserCreationForm):

    def clean_username(self):
        return self.cleaned_data.get("username")
