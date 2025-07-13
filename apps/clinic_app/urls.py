from django.urls import path
from .views import (
    clinicView,
    patientView,
    createPatientView,
    ListDrugView,
    DeleteDrug,
    createDrugView,
)

urlpatterns = [
    path('', clinicView.as_view(), name='clinic'),
    path('patients/', patientView.as_view(), name='patients'),
    path('patient/create/', createPatientView.as_view(), name='create-patient'),
    path('patient/<slug:slug>/edit/', createPatientView.as_view(), name='edit-patient'),
    
    path('drug/list/', ListDrugView.as_view(), name="list-drugs"),
    path('drug/add/', createDrugView.as_view(), name="add-drug"),
    path('drug/<slug:slug>/edit/', createDrugView.as_view(), name="edit-drug"),
    path('drug/<slug:slug>/delete/', DeleteDrug.as_view(), name="delete-drug"),
]