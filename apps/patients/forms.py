from django import forms
from .models import Patient



class PatientForm(forms.ModelForm):
    dateOfBirth = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Patient
        fields = [
            'firstName',
            'lastName',
            'dataOfBirth',
            'contact',
            'gender',
            'bloodType',
            'allergies',
            'account',
        ]