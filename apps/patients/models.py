import uuid
from django.db import models
from django.contrib.auth import get_user_model

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)
BLOOD_TYPE = (
    ('A', 'A'),
    ('B', 'B'),
    ('AB', 'AB'),
    ('O', 'O')
)

class Patient(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    userID      = models.CharField(max_length=250, unique=True, blank=True, verbose_name="Matric ID", null=True, help_text="Matric Number of student")
    firstName   = models.CharField(max_length=250, verbose_name="First Name", blank=True, null=True)
    lastName    = models.CharField(max_length=250, verbose_name="Last Name", blank=True, null=True)
    dateOfBirth = models.DateField(verbose_name="Date of Birth", blank=True, null=True)
    bloodType   = models.CharField(max_length=5, verbose_name="Blood Type", choices=BLOOD_TYPE, default='O')
    allergy     = models.TextField(blank=True, null=True, help_text='List of allergies')
    gender      = models.CharField(max_length=10, choices=GENDER, default='M')
    contact     = models.CharField(max_length=20, verbose_name="Phone Number", blank=True, null=True, help_text='Phone number')
    account     = models.OneToOneField(
        get_user_model(), 
        verbose_name="Patient Account",
        help_text="Patient Account",
        on_delete=models.CASCADE, 
        related_name='patient', 
        related_query_name='patient')
    
    def get_fullName(self):
        return f" {self.firstName}  {self.lastName} "
    
    def short_name(self):
        return str(self.firstName)
    
    def __str__(self):
        return self.get_fullName()
    
    

class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE
    )
    staff = models.ForeignKey(
        'staff.Staff', on_delete=models.CASCADE
    )
    
    comment = models.TextField(blank=True, null=True)
    
    date_created = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.pk)