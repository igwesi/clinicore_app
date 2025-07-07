from django.shortcuts import render, redirect
from django.views import View
from apps.accounts.forms import LoginForm, RegisterForm


class dashboardView(View):
    def get(self, request):
        return render(request, 'user/staff/dashboard.html')    

def searchPatient(request):
    if request.GET.get('patient') is not None:
        query_text = request.GET.get('patient')
            
        return render(request, 'user/staff/dashboard.html', {'query_text': query_text})
    return redirect('dashboard')
    