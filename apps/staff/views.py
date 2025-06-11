from django.shortcuts import render, redirect
from django.views import View
from apps.accounts.forms import LoginForm, RegisterForm


class dashboardView(View):
    def get(self, request):
        return render(request, 'user/staff/dashboard.html')


class loginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'registrations/login.html', {'form': form})