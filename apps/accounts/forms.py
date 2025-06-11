from django import forms
from captcha.fields import CaptchaField, BaseCaptchaTextInput

class LoginForm(forms.Form):
    email = forms.CharField(max_length=150, required=True, widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    show_password = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={'class': 'hide-password', 'id': 'hide_password'}))
    remember_me = forms.BooleanField(required=False, initial=False)
    captcha = CaptchaField()
    # Add any additional fields you need for your login form    


class RegisterForm(forms.Form):
    email       = forms.CharField(max_length=150, required=True, widget=forms.EmailInput(attrs={'placeholder':'hello@example.com'}))
    password    = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'********'}), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'********'}), required=True)
    captcha = CaptchaField()