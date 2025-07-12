from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from apps.accounts.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from .models import Patient




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
        
        return redirect('Staff:dashboard')

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