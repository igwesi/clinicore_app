from django import forms
from captcha.fields import CaptchaField, BaseCaptchaTextInput
from apps.patients.models import Patient
from apps.staff.models import Staff, ROLE as STAFF_ROLES
from apps.patients.forms import PatientForm
# from apps.clinic_app.forms import yzz



class LoginForm(forms.Form):
    email = forms.CharField(max_length=150, required=True, widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    show_password = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={'class': 'hide-password', 'id': 'hide_password'}))
    # captcha = CaptchaField()
    # Add any additional fields you need for your login form    


class RegisterForm(forms.Form):
    email       = forms.CharField(max_length=150, required=True, widget=forms.EmailInput(attrs={'placeholder':'hello@example.com'}))
    password    = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'********'}), required=True)
    # confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'********'}), required=True)
    # captcha = CaptchaField()
    

class StaffForm(forms.ModelForm):
    firstName   = forms.CharField(max_length=250, required=True)
    lastName    = forms.CharField(max_length=250, required=True)
    role        = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=STAFF_ROLES, required=True)
    contact     = forms.CharField(max_length=20, required=True, help_text='Phone number')
    
    class Meta:
        model = Staff
        fields = ["firstName", "lastName", "role", "contact"]