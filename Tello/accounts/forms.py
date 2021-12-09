from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm,UsernameField
from .models import User, Order
from django.contrib.auth.forms import PasswordChangeForm

PAYMENT_CHOICES = (
    ("Onlayn kart ilə ödəmə", ("Onlayn kart ilə ödəmə")),
    ("Qapıda nağd ödəmə", ("Qapıda nağd ödəmə"))
)


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

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['full_name', 'email', 'number', 'birth_date']

        widgets = {
            'full_name': forms.TextInput(attrs={'id': 'full_name', 'placeholder': 'First Name',  'class': 'profile-infp-inp'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Bio',  'class': 'profile-infp-inp'}),
            'number': forms.NumberInput(attrs={'id': 'phone', 'placeholder': '123-456-7890', 'class': 'profile-infp-inp', 'pattern': '[0-9]{3}-[0-9]{2}-[0-9]{3}'}),
            'birth_date': forms.DateInput(attrs={'id': 'date', 'placeholder': '2021-10-30', 'class': 'profile-infp-inp'}),
        }

class ThePasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Cari şifrənizi daxil edin',
                'class' : 'profile-infp-inp',
            }))

    new_password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Yeni şifrənizi daxil edin',
                'class' : 'profile-infp-inp',
            }))

    new_password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Yeni şifrənizi yenidən daxil edin',
                'class' : 'profile-infp-inp',
            }))

class CreateOrderForm(forms.ModelForm):
    payment_type = forms.ChoiceField(choices=PAYMENT_CHOICES,
    widget=forms.RadioSelect)

    class Meta:
        model = Order
        fields = ['customer_name', 'customer_surname', 'customer_number', 'customer_adress', 'customer_home_number', 'message_for_courier', 'customer_email', 'payment_type']

        widgets = {
            'customer_name': forms.TextInput(attrs={'id': 'first_name', 'placeholder': 'Adınızı daxil edin',  'class': 'payment-inputs'}),
            'customer_surname': forms.TextInput(attrs={'id': 'last_name', 'placeholder': 'Soyadınızı daxil edin',  'class': 'payment-inputs'}),
            'customer_number': forms.TextInput(attrs={'id': 'number', 'placeholder': '000 - 00 - 00',  'class': 'payment-inputs'}),
            'customer_adress': forms.TextInput(attrs={'id': 'customer_adress', 'placeholder': 'Ünvanı daxil edin',  'class': 'payment-inputs'}),
            'customer_home_number': forms.TextInput(attrs={'id': 'customer_home_number', 'placeholder': 'Daxil edin',  'class': 'payment-inputs'}),
            'message_for_courier': forms.Textarea(attrs={'id': 'message_for_courier', 'placeholder': 'Mətni daxil edin...',  'class': 'payment-textarea'}),
            'customer_email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'nümunə@gmail.com',  'class': 'payment-inputs'}),
        }