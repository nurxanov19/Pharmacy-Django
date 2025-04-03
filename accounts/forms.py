from django.core.exceptions import ValidationError

from .models import User
from django.forms import ModelForm, Form
from django import forms


class UserForm(ModelForm):

    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Confirmation password is wrong')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hashes the password
        if commit:
            user.save()
        return user
