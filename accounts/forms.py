from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Saisir un nouveau mot de passe'
        }), label="Mot de passe")
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Confirmez votre mot de passe'
        }), label="Répéter votre mot de passe")


    class Meta:
        model = CustomUser
        fields = ('email', 'username')

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Saisir votre nom d\'utilisateur ici'
                }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'Saisir votre adresse-email ici'
                }),
        }

        help_texts = {
            'username': None,
        }



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username')