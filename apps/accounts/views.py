from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from apps.clinic_app.models import Patient


class dashboardView(View):
    def user_authenticated(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        return request.user.is_authenticated
    
    def patient(self, request):
        return redirect('patient:dashboard')
    
    def staff(self, request):
        return redirect('Staff:dashboard')
    
    def get(self, request):
        patient_count = Patient.objects.all().count()
        self.user_authenticated(request)
        if request.user.role == 'staff':
            return self.staff(request)
        elif request.user.role == 'patient':
            return self.patient(request)
        return render(request, 'core/dashboard.html', {
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
            remember_me = form.cleaned_data['remember_me']
            
            if get_user_model().objects.filter(email=email).exists():
                # Check if the user is a human
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    if remember_me:
                        request.session.set_expiry(1209600)
                    else:
                        request.session.set_expiry(0)
                    return redirect('dashboard')
                else:
                    # If the user is not authenticated, check if the username and password are correct
                    form.add_error(None, 'Invalid username or password')
                    human = False
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
            confirm_password = form.cleaned_data['confirm_password']
            
            if get_user_model().objects.filter(email=email).exists():
                form.add_error(None, 'Account already exists')
                return render(request, 'registrations/register.html', {'form': form})
            
            # Check if the passwords match
            if password == confirm_password:
                user = get_user_model().objects.create_user(email=email, password=password, role='patient')
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, 'Passwords do not match')
                return render(request, 'registrations/register.html', {'form': form})
        else:
            form.add_error(None, 'Invalid form submission')
            return render(request, 'registrations/register.html', {'form': form})        
    

class logoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")