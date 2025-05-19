from django.urls import path
from .views import (
    clinicView,
    # doctorView,
    # patientView,
    # appointmentView,
    # prescriptionView,
    # medicalHistoryView,
    # billingView,
    # reportView,
    # feedbackView,
)

urlpatterns = [
    path('', clinicView.as_view(), name='clinic'),
    # path('doctors/', doctorView.as_view(), name='doctors'),
    # path('patients/', patientView.as_view(), name='patients'),
    # path('appointments/', appointmentView.as_view(), name='appointments'),
    # path('prescriptions/', prescriptionView.as_view(), name='prescriptions'),
    # path('medical-history/', medicalHistoryView.as_view(), name='medical-history'),
    # path('billing/', billingView.as_view(), name='billing'),
    # path('reports/', reportView.as_view(), name='reports'),
    # path('feedback/', feedbackView.as_view(), name='feedback'),
]