import uuid
from django.db import models
from django.contrib.auth import get_user_model

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Prefer not to say')
)
BLOOD_TYPE = (
    ('A', 'A'),
    ('B', 'B'),
    ('AB', 'AB'),
    ('O', 'O')
)

class Patient(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    userID      = models.CharField(max_length=250, unique=True, help_text="Matric Number of student")
    firstName   = models.CharField(max_length=250, blank=False)
    lastName    = models.CharField(max_length=250, blank=False)
    dataOfBirth = models.DateField()
    bloodType   = models.CharField(max_length=5, choices=BLOOD_TYPE, default='O')
    allergies   = models.TextField(blank=True, null=True, help_text='List of allergies')
    gender      = models.CharField(max_length=10, choices=GENDER, default='M')
    contact     = models.CharField(max_length=20, unique=True, help_text='Phone number')
    account     = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='patient', related_query_name='patient')
    
    def get_fullName(self):
        return f" {self.firstName}  {self.lastName} "
    
    def short_name(self):
        return str(self.firstName)
    
    def __str__(self):
        return self.get_fullName()