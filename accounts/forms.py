
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
#from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email"
        )


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password",)
