from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import AccountManager
from django.contrib.auth.models import UserManager

class Account(AbstractUser):
    ROLES = (
        ('patient', 'Patient'),
        ('staff', 'Staff'),
        ('admin', 'Admin')
    )
    username    = None  # Remove the username field
    first_name  = None
    last_name   = None
    email       = models.EmailField(unique=True, primary_key=True)
    role        = models.CharField(max_length=30, choices=ROLES)
    last_login  = models.DateTimeField(null=True, blank=True)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    objects     = AccountManager()  # Default manager
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
        
    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Account'
        ordering = ['email']