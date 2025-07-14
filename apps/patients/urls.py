from django.urls import path
from .views import *

app_name = 'Patient'

urlpatterns = [
    path('', patientDashboard.as_view(), name='dashboard'),
    path('add/', AddPatientView.as_view(), name='add_patient'),
    path('edit/<uuid:patient_id>/', AddPatientView.as_view(), name='edit_patient'),
    path('all_patients/', allPatients.as_view(), name='all_patients'),
    path('search-patient', searchPatient.as_view(), name='search_patient'),
    path('info/<uuid:patient_id>/', patientDetails.as_view(), name='patient_detail'),
]
