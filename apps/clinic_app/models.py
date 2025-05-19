from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils import timezone

User_Model = get_user_model()


class Patient(models.Model):
    PatientType = (
        ('inpatient', 'Inpatient'),
        ('outpatient', 'Outpatient'),
        ('emergency', 'Emergency'),
    )

    ROLE = (
        ('student', 'Student'),
        ('staff', 'Staff'),
    )

    user            = models.OneToOneField(User_Model, on_delete=models.CASCADE)
    first_name      = models.CharField(max_length=200)
    last_name       = models.CharField(max_length=200)
    blood_type      = models.CharField(max_length=5)
    gender          = models.CharField(max_length=10)
    patient_type    = models.CharField(max_length=20, choices=PatientType)
    role            = models.CharField(max_length=50, choices=ROLE, default='student')
    allergies       = models.TextField()
    
    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patient'
        ordering = ['-id']
    def get_full_name(self):
        return self.first_name + ' ' +self.last_name  
    def __str__(self):
        return self.get_full_name()+ " - "+self.user.email
    

class Drug(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expiration_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Drug'
        verbose_name_plural = 'Drug'
        ordering = ['-id']

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    date_prescribed = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='active')
    class Meta:
        verbose_name = 'Prescription'
        verbose_name_plural = 'Prescription'
        ordering = ['-id']
        

class PrescriptionItem(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Prescription Item'
        verbose_name_plural = 'Prescription Item'
        ordering = ['-id']
        
class Dispensation(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    pharmacist = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    date_dispensed = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    
    class Meta:
        verbose_name = 'Dispensation'
        verbose_name_plural = 'Dispensation'
        ordering = ['id']

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default='scheduled')
    
    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointment'
        ordering = ['-datetime']