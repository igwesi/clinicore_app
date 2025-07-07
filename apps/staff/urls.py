from django.urls import path
from .views import *


app_name = "Staff"

urlpatterns = [
    path('', dashboardView.as_view(), name='dashboard'),
    path('search-patient', searchPatient, name='search-patient'),
]