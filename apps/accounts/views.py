from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from apps.clinic_app.models import Patient
from apps.clinic_app.models import Staff
from .forms import (
    LoginForm, 
    RegisterForm, 
    PatientForm, 
    StaffForm
)


Account = get_user_model()


def authView(request):
    return redirect('login')

class dashboardView(View):
    def user_authenticated(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        return request.user.is_authenticated
    
    def patient(self, request):
        return redirect('Patient:dashboard')
    
    def staff(self, request):
        return redirect('Staff:dashboard')
    
    def get(self, request):
        patient_count = Patient.objects.all().count()
        self.user_authenticated(request)

        if request.user.role == 'staff':
            return self.staff(request)
        elif request.user.role == 'patient':
            return self.patient(request)

        return render(request, 'user/patient/dashboard.html', {
            'patient_count': patient_count
        })

class loginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'registrations/login.html', {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            human = True
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            if get_user_model().objects.filter(email=email).exists():
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    # If the user is not authenticated, check if the username and password are correct
                    form.add_error(None, 'Invalid username or password')
            else:
                form.add_error(None, 'Account does not exist')
                human = False
        else:
            form.add_error(None, 'Invalid form submission')
        return render(request, 'registrations/login.html', {'form': form})



class registerView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'registrations/register.html', {'form':form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            if get_user_model().objects.filter(email=email).exists():
                form.add_error(None, 'Account already exists')
                return render(request, 'registrations/register.html', {'form': form})
            
            user = get_user_model().objects.create_user(email=email, password=password, role='patient')
            login(request, user)
            return redirect('auth-role-selection')
        else:
            form.add_error(None, 'Invalid form submission')
            return render(request, 'registrations/register.html', {'form': form})        

class logoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
    
    
class AuthRoleSelection(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        
        return render(request, 'registrations/role-selection.html')

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        
        role = request.POST.get('auth-role')
        account = Account.objects.get(email=request.user.email)
        
        if role == 'patient':
            account.role = role.lower()
            Patient.objects.get_or_create(account=account)
            account.save()
            return redirect("auth-profile-setup")
        
        if role == 'staff':
            account.role = role.lower()
            Staff.objects.get_or_create(account=account)
            account.save()
            return redirect('auth-profile-setup')
        
        messages.error(request, 'Invalid role selected')        
        return redirect('auth-role-selection')
    


class AuthProfileSetup(View):
    def PatientProfile(self, request):
        form = PatientForm()
        
        if request.POST:
            form = PatientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
            messages.error(request, form.errors)
            
        return render(request, 'registrations/auth-profile-setup.html', {'form': form})
    
    def AdminProfile(self, request):
        form = StaffForm()
        if request.POST:
            form = StaffForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
            messages.error(request, form.errors)
        return render(request, 'registrations/auth-profile-setup.html', {'form': form})
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        if request.user.role == 'patient':
            return self.PatientProfile(request)
        
        elif request.user.role == 'staff':
            return self.AdminProfile(request)
        
        return redirect('auth-role-selection')
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        if request.user.role == 'patient':
            form = PatientForm(request.POST)
            
            if form.is_valid():
                instance = form.save(commit=False)
                instance.account = request.user
                instance.save()
                return redirect('dashboard')        

        if request.user.role == 'staff':
            form = StaffForm(request.POST)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.account = request.user
                instance.save()
                return redirect('dashboard')

        messages.error(request, form.errors)    
        return redirect('dashboard')