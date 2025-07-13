from django import forms
from apps.patients.models import Patient
from .models import Appointment, DrugInventory

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["firstName", "lastName", "bloodType", "gender", "contact" , "allergies"]
        

class EditPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["firstName", "lastName", "bloodType", "gender", "contact" , "allergies"]
        
        
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["doctor", "reason", "status", "comment", "datetime"]


class DrugInventoryForm(forms.ModelForm):
    class Meta:
        model = DrugInventory
        fields = ["name", "manufacturer", "quantity", "expiration_date"]

