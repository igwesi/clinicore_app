from django.urls import path
from .views import *

app_name = 'Patient'

urlpatterns = [
    path('', patientDashboard.as_view(), name='dashboard'),
]
