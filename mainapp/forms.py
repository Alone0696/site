from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from mainapp.models import Mainapp


class AddText(forms.Form):
    text = forms.CharField(label='',required=False,widget=forms.Textarea(attrs={'cols':'38','rows':'10'}))





class RegisterForm(UserCreationForm):
    username = forms.CharField(label = '',widget=forms.TextInput(attrs={'placeholder':'Придумайте логин','class':'form-input'}))
    password1 = forms.CharField(label = '',widget=forms.PasswordInput(attrs={'placeholder':'Придумайте пароль','class':'form-input'}))
    password2 = forms.CharField(label = '',widget=forms.PasswordInput(attrs={'placeholder':'Повторите пароль','class':'form-input'}))

    class Meta:
        model = User
        fields = ('username','password1','password2')
        widgets = {
            'username':forms.TextInput(),
            'password1':forms.PasswordInput(),
            'password2':forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False})


class LoginForm(AuthenticationForm):
    username = forms.CharField(label = '',widget=forms.TextInput(attrs={'placeholder':'Логин','class':'form-input'}))
    password = forms.CharField(label = '',widget=forms.PasswordInput(attrs={'placeholder':'Пароль','class':'form-input'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False})