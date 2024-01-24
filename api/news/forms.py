from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from news.models import News

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-4 px-6 rounded shadow',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'w-full py-4 px-6 rounded shadow',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-4 px-6 rounded shadow',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-4 px-6 rounded shadow',
    }))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-4 px-6 rounded shadow',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-4 px-6 rounded shadow',
    }))

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'picture']
    
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-4 px-6 rounded shadow',
    }))

    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'w-full py-4 px-6 rounded shadow',
    }))
    
    picture = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'w-full py-4 px-6 rounded shadow',
    }))