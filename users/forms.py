from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm,PasswordResetForm
from django.core.exceptions import ValidationError
from .models import Profile
from django.contrib.auth import get_user_model

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()

    def clean_email(self):
        data = self.cleaned_data["email"]
        if "@nitkkr.ac.in" not in data:
            raise ValidationError("Please Register through your Nit KKR domain mail only!")
        return data

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    # email= forms.EmailField()

    class Meta:
        model=User
        fields=['username']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=['image']

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)