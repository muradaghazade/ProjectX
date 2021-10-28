from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm,UsernameField
from .models import User
# from django_range_slider.fields import RangeSliderField


class RegisterForm(UserCreationForm):

    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'password',
                'class' : 'fullname-inp',
            }))

    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'confirm password',
                'class' : 'fullname-inp',
            }))

    class Meta:
        model = User
        fields = ('full_name','email','password1','password2', 'number')

        widgets = {
            'full_name': forms.TextInput(attrs={'id': 'fullname', 'placeholder': 'Ad və soyadınızı daxil edin', 'class': 'fullname-inp'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'nümunə@gmail.com', 'class': 'fullname-inp'}),
            'number': forms.NumberInput(attrs={'id': 'phone', 'placeholder': '000-00-00', 'class': 'fullname-inp'}),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'class': 'fullname-inp',
        'placeholder': 'Email',
        'name': 'email'
    }))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'fullname-inp',
            'name': 'password',
            'placeholder': 'Password'
        }),
    )

    class Meta:
        model = User
        fields = ['username', 'password']