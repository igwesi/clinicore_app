from django import forms
from apps.patients.models import Patient
from .models import Appointment, DrugInventory
from django import forms
from django.core.exceptions import ValidationError
import datetime
import calendar

class ExpirationDateField(forms.DateField):
    """Custom form field for drug expiration dates with month/year validation"""
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', forms.DateInput(attrs={
            'type': 'date',  # Uses HTML5 month input type
            'min': datetime.date.today().strftime('%Y-%m-%d'),
            'placeholder': 'DD/MM/YYYY'
        }))
        super().__init__(*args, **kwargs)
        self.help_text = "Format: DD/MM/YYYY"
    
    def to_python(self, value):
        """Convert input to datetime.date object"""
        if not value:
            return None
        
        # Handle full date strings (YYYY-MM-DD)
        if isinstance(value, datetime.date):
            return value
        
        # Handle month-year format (YYYY-MM)
        if isinstance(value, str) and len(value) == 7:
            try:
                year, month = map(int, value.split('-'))
                last_day = calendar.monthrange(year, month)[1]
                return datetime.date(year, month, last_day)
            except (ValueError, IndexError):
                raise ValidationError("Enter a valid date in YYYY-MM-DD format")
        
        return super().to_python(value)
    
    def validate(self, value):
        """Validate expiration date"""
        super().validate(value)
        
        if value:
            # Ensure date is in the future
            if value < datetime.date.today():
                raise ValidationError("Expiration date must be in the future")
            
            # Ensure date is not too far in future (pharma industry standard)
            max_date = datetime.date.today() + datetime.timedelta(days=365*5)  # 5 years max
            if value > max_date:
                raise ValidationError("Expiration date cannot be more than 5 years in future")
    
    def prepare_value(self, value):
        """Convert date to YYYY-MM format for display"""
        if isinstance(value, datetime.date):
            return value.strftime('%Y-%m-%d')
        return value
    

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
    expiration_date = ExpirationDateField(
        label="Expiration Date",
        required=True
    )
    class Meta:
        model = DrugInventory
        fields = ["name", "purpose", "usage", "manufacturer", "quantity", "expiration_date"]


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["doctor", "reason", "status", "comment", "datetime"]
    
    def clean_datetime(self):
        datetime = self.cleaned_data.get('datetime')
        if datetime < datetime.now():
            raise forms.ValidationError("Appointment date and time cannot be in the past.")
        return datetime