from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from apps.clinic_app.models import Patient


class dashboardView(View):
    def user_authenticated(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        return request.user.is_authenticated
    
    def get(self, request):
        patient_count = Patient.objects.all().count()
        self.user_authenticated(request)
        return render(request, 'core/dashboard.html', {
            'patient_count': patient_count
        })



class loginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'registrations/login.html', {'form': form})
    
    def post(self, request):
        print(request.POST)
        form = LoginForm(request.POST)
        
        if form.is_valid():
            human = True
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            captcha = form.cleaned_data['captcha']
            
            if get_user_model().objects.filter(email=email).exists():
                # Check if the user is a human
                user = authenticate(request, email=email, password=password)
                
                if user is not None:
                    login(request, user)
                    if remember_me:
                        request.session.set_expiry(1209600)
                    else:
                        request.session.set_expiry(0)
                    return redirect('clinic')
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
        return render(request, 'registrations/register.html')
    
    def post(self, json):
        # Handle registration logic here
        pass