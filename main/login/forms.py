from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User 

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','user_type', 'email', 'password1', 'password2', )
