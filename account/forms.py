from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import MyUser


class UserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name',
                  'contact', 'password1', 'password2','user_Role','address')
        widgets = {
            'user_Role': forms.HiddenInput(attrs={'value': 'customer'})
        }



class AdminForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name',
                  'contact', 'password1','password2', 'user_Role','address')
        widgets = {
            'user_Role': forms.HiddenInput(attrs={'value': 'admin'})
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['password1'].help_text = None
    #     self.fields['password2'].help_text = None
