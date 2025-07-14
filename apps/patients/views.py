from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from apps.accounts.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from .forms import Patient, PatientForm
from apps.clinic_app.forms import AppointmentForm
from apps.clinic_app.models import Appointment





@method_decorator(login_required, name='dispatch')
class patientDashboard(View):
    def get(self, request):
        return render(request, 'user/patient/dashboard.html')
    

class searchPatient(View):
    def get(self, request):
        query_text = request.GET['patient'] if 'patient' in request.GET else None
        
        if query_text:
            print(query_text)
            # Assuming you have a method to search patients by name or ID
            patients = Patient.objects.filter(userID__icontains=query_text) 
            print(patients) 
            return render(request, 'user/patient/search_results.html', {'patients': patients, 'query_text': query_text})
        
        return redirect('Patient:all_patients')

class allPatients(View):
    def get(self, request):
        all_patients = Patient.objects.all()
        return render(request, 'user/patient/all_patients.html', {'patients': all_patients})        


class patientDetails(View):
    def get(self, request, patient_id):
        try:
            patient = Patient.objects.get(id=patient_id)
            return render(request, 'user/patient/details.html', {'patient': patient})
        except Patient.DoesNotExist:
            return redirect('Staff:dashboard')


class AddPatientView(View):
    template_name = 'core/patients/create-patient.html'
    
    def get(self, request):
        form = PatientForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Patient added successfully")
            return redirect('dashboard')
        messages.error(request, form.errors)
        return render(request, self.template_name, {'form': form})


class BookAppointment(View):

    def get(self, request):
        user = request.user        
        try:
            if user.role == 'patient':
                appointments = Appointment.objects.filter(patient__account=user)
            else:
                appointments = Appointment.objects.all(staff__account=user)
            
            form   = AppointmentForm()    
            return render(request, 'user/book_appointment.html', {'form': form, 'appointments': appointments})
    
        except Appointment.DoesNotExist:
            return redirect('Staff:dashboard')
    
    def post(self, request):
        user = request.user
        
        form   = AppointmentForm(request.POST)
        patient = Patient.objects.get(account=user)
        
        if form.is_valid():
            appointment = form.save(commit=False)          
            appointment.patient = patient
            appointment.save()
        
        return render(request, 'user/book_appointment.html', {'form': form})