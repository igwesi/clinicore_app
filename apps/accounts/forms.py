from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    email = forms.CharField(max_length=150, required=True, widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    remember_me = forms.BooleanField(required=False, initial=False)
    captcha = CaptchaField()
    # Add any additional fields you need for your login form    