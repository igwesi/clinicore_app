from django import forms
from apps.patients.models import Patient

# from .models import (
    # Drug,
    # Appointment,
    # Dispensation,
    # Prescription,
    # PrescriptionItem,
# )

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["firstName", "lastName", "bloodType", "gender", "contact" , "allergies"]
        

class EditPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["firstName", "lastName", "bloodType", "gender", "contact" , "allergies"]
        

# class DrugForm(forms.ModelForm):
#     name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Drug name'}))
#     expiration_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
#     class Meta:
#         model = Drug
#         fields = "__all__"

