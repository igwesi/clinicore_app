from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.accounts.forms import LoginForm, RegisterForm
from apps.patients.models import Patient
from apps.clinic_app.models import Appointment, DrugInventory

class dashboardView(View):
    queryset = Patient.objects.all()
    
    def get(self, request):
        context = []
        all_patients = Patient.objects.all()
        drugs = DrugInventory.objects.all()
        appointments = Appointment.objects.all()
        context = {
            'drugs': drugs,
            'patients': all_patients,
            'appointments': appointments,
            'query_text': request.GET.get('patient', None)
        }
        return render(request, 'user/staff/dashboard.html', context)    

def searchPatient(request):
    if request.GET.get('patient') is not None:
        query_text = request.GET.get('patient')
            
        return render(request, 'user/staff/dashboard.html', {'query_text': query_text})
    return redirect('dashboard')
    