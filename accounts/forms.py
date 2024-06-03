
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "addressCustomer",
            "numberAddress",
            "city",
            "cap",
        )


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "password",)
