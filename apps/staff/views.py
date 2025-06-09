from django.shortcuts import render, redirect
from django.views import View
from apps.accounts.forms import LoginForm, RegisterForm


class staffDashboard(View):
    def get(self, request):
        return render(request, 'core/staff/dashboard.html')


class staffLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'registrations/login.html', {'form': form})