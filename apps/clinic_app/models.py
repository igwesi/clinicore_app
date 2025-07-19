from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from apps.patients.models import Patient
from apps.staff.models import Staff


APPOINTMENT_STATUS = [
    ('scheduled', 'scheduled'),
    ('cancelled', 'cancelled'),
    ('completed', 'completed')

]

class Appointment(models.Model):
    patient     = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor      = models.ForeignKey(Staff, on_delete=models.CASCADE)
    
    reason      = models.TextField(blank=True)
    
    status      = models.CharField(max_length=20, choices=APPOINTMENT_STATUS, default='scheduled')
    
    comment     = models.TextField(blank=True)
    datetime    = models.DateField()
    
    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointment'
        ordering = ['-datetime']
        
    def __str__(self):
        return str(self.patient.get_full_name())
        


class DrugInventory(models.Model):
    name                = models.CharField(max_length=100)
    manufacturer        = models.CharField(max_length=100)
    purpose             = models.CharField(max_length=200, blank=True, null=True)
    usage               = models.CharField(max_length=200, blank=True, null=True)
    quantity            = models.IntegerField(default=0)
    expiration_date     = models.DateField()
    last_updated        = models.DateField(auto_now_add=True)

    def is_available(self):
        return True if self.quantity > 0 else False
    def __str__(self):return str(self.name)
    class Meta:
        verbose_name = 'Drug'
        verbose_name_plural = 'Drug'
        ordering = ['-id']