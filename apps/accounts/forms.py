from django import forms
from captcha.fields import CaptchaField, BaseCaptchaTextInput
from apps.patients.models import Patient
from apps.staff.models import Staff



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
    

class PatientForm(forms.ModelForm):
    firstName   = forms.CharField(max_length=250, required=True)
    lastName    = forms.CharField(max_length=250, required=True)
    userID      = forms.CharField(max_length=250, required=True)
    dataOfBirth = forms.DateField(required=True)
    bloodType   = forms.ChoiceField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], required=True)
    allergies   = forms.CharField(max_length=250, required=True)
    gender      = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], required=True)
    contact     = forms.CharField(max_length=20, required=True, help_text='Phone number')
    
    class Meta:
        model = Patient
        fields = ["firstName", "lastName", "userID", "dataOfBirth", "bloodType", "allergies", "gender", "contact"]
    


class AdminForm(forms.ModelForm):
    firstName    = forms.CharField(max_length=250, required=True)
    lastName    = forms.CharField(max_length=250, required=True)
    role        = forms.ChoiceField(choices=[('doctor', 'Doctor'), ('nurse', 'Nurse')], required=True)
    contact     = forms.CharField(max_length=20, required=True, help_text='Phone number')
    
    class Meta:
        model = Staff
        fields = ["firstName", "lastName", "role", "contact"]