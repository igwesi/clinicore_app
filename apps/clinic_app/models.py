from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from apps.patients.models import Patient
from apps.staff.models import Staff

class Appointment(models.Model):
    patient     = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor      = models.ForeignKey(Staff, on_delete=models.CASCADE)
    
    reason      = models.TextField(blank=True)
    status      = models.CharField(max_length=20, choices=[
                        ('scheduled', 'scheduled'),
                        ('cancelled', 'cancelled'),
                        ('completed', 'completed')
                ], default='scheduled')
    comment     = models.TextField(blank=True)
    datetime    = models.DateTimeField()
    
    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointment'
        ordering = ['-datetime']
        
    def __str__(self):
        return str(self.patient.get_full_name())
        


# class Drug(models.Model):
#     name                = models.CharField(max_length=100)
#     manufacturer        = models.CharField(max_length=100)
#     quantity            = models.IntegerField(default=0)
#     expiration_date     = models.DateField()
#     price               = models.DecimalField(max_digits=10, decimal_places=2)
#     last_updated        = models.DateField(auto_now_add=True)

#     def is_available(self):
#         return True if self.quantity > 0 else False

#     class Meta:
#         verbose_name = 'Drug'
#         verbose_name_plural = 'Drug'
#         ordering = ['-id']


# class Prescription(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     doctor  = models.ForeignKey(Staff, on_delete=models.CASCADE)
#     comment = models.TextField(blank=True)
#     date_prescribed = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, default='active')
    
#     class Meta:
#         verbose_name = 'Prescription'
#         verbose_name_plural = 'Prescription'
#         ordering = ['-id']

# class PrescriptionItem(models.Model):
#     prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
#     drug        = models.ForeignKey(Drug, on_delete=models.CASCADE)
#     dosage      = models.CharField(max_length=50, blank=True)
#     frequency   = models.CharField(max_length=50, blank=True)
#     duration    = models.CharField(max_length=50, blank=True)

#     class Meta:
#         verbose_name = 'Prescription Item'
#         verbose_name_plural = 'Prescription Item'
#         ordering = ['-id']
        
# class Dispensation(models.Model):
#     prescription    = models.ForeignKey(Prescription, on_delete=models.CASCADE)
#     pharmacist      = models.ForeignKey(Staff, on_delete=models.CASCADE)
#     date_dispensed  = models.DateTimeField(auto_now_add=True)
#     quantity        = models.IntegerField()
    
#     class Meta:
#         verbose_name = 'Dispensation'
#         verbose_name_plural = 'Dispensation'
#         ordering = ['id']