from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from apps.accounts.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model




@method_decorator(login_required, name='dispatch')
class patientDashboard(View):
    def get(self, request):
        return render(request, 'user/patient/dashboard.html')