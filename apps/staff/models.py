import uuid
from django.db import models
from django.contrib.auth import get_user_model

# Defining the distinct roles
ROLE = (
    ('doctor', 'Doctor'),
    ('nurse', 'Nurse'),
    ('admin', 'Admin'),
    ('staff', 'Staff')
)

class Staff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    firstName   = models.CharField(max_length=200, blank=True, null=True)
    lastName    = models.CharField(max_length=200, blank=True, null=True)
    role        = models.CharField(max_length=200, blank=True, null=True, choices=ROLE, default='doctor')
    contact     = models.CharField(max_length=20, help_text='Phone number', blank=True, null=True)
    account     = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True, related_query_name='staff', related_name='staff')
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
    def is_admin(self):
        return self.role == 'admin'

    def is_staff(self):
        return self.role == 'staff'

    def is_doctor(self):
        return self.role == 'doctor'
    
    def is_nurse(self):
        return self.role == 'nurse'
    
    def role(self):
        return self.role