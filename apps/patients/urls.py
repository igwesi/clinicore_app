from django.urls import path
from .views import *

app_name = 'patient'

urlpatterns = [
    path('', patientDashboard.as_view(), name='dashboard'),
]
