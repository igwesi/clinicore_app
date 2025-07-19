from django import forms
from .models import Patient, BLOOD_TYPE, GENDER
from apps.accounts.models import Account


def ACCOUNT_DICT():
    all_accounts = Account.objects.all().exclude(role='staff')
    to_dict = []
    for account in all_accounts:
        
        to_dict.append((account.email, account.email))
    return to_dict


class PatientForm(forms.ModelForm):
    firstName       = forms.CharField(label='*First Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'' }))
    lastName        = forms.CharField(label='*Last Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'' }))
    contact         = forms.CharField(label='*Phone Number', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'' }))
    allergy         = forms.CharField(label='*Allergy', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'' }))
    dateOfBirth     = forms.DateField(label="*Date of Birth", widget=forms.DateInput(attrs={'type':'date'}))
    gender          = forms.ChoiceField(label='*Gender', widget=forms.Select(attrs={'class':'form-control'}), choices=GENDER)
    bloodType       = forms.ChoiceField(label='*Blood Type', widget=forms.Select(attrs={'class':'form-control'}), choices=BLOOD_TYPE, required=True)
    account         = forms.ChoiceField(label="*Patient's Email", widget=forms.Select(attrs={'class':'form-control', 'placeholder':''}), required=True, choices=ACCOUNT_DICT())
    
    class Meta:
        model = Patient
        fields = [
            'userID',
            'firstName',
            'lastName',
            'contact',
            'dateOfBirth',
            'gender',
            'bloodType',
            'allergy',
            'account',
        ]