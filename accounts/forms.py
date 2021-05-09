from .models import Account
from django.contrib.auth.forms import UserCreationForm
from django import forms


class AccountCreationForm(UserCreationForm):
    """Форма для регистрации пользователя"""
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = Account
        fields = ['account_login', 'account_phone',
                  'account_email', 'password1', 'password2']
        widgets = {
            'account_login': forms.TextInput(attrs={'placeholder': 'Введите логин'}),
            'account_phone': forms.TextInput(attrs={'placeholder': 'Введите номер телефона'}),
            'account_email': forms.TextInput(attrs={'placeholder': 'Введите почту'}),
        }
