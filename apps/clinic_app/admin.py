from django.contrib import admin
from .models import Patient, DrugInventory, Appointment

admin.site.register(Patient)
admin.site.register(DrugInventory)
admin.site.register(Appointment)