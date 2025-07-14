from django.shortcuts import render, redirect
from django.views import View, generic
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from apps.patients.models import Patient

from apps.accounts.forms import (
    RegisterForm,
)

from .forms import (
    PatientForm,
    EditPatientForm,
    DrugInventoryForm
)

from .models import DrugInventory, Appointment

class clinicView(LoginRequiredMixin, TemplateView):
    template_name = 'core/clinic.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    

class patientView(LoginRequiredMixin, View):
    template_name = 'core/patients/view-patient.html' 
    
    def get(self, request):
        patients = Patient.objects.all().order_by('id')
        return render(request,
            self.template_name,
            {'patients': patients})


class createPatientView(LoginRequiredMixin, generic.UpdateView):
    create_template = 'core/patients/create-patient.html'
    update_template = 'core/patients/update-patient.html'

    def get(self, request, slug=None):
        # Render Patient Instance Form
        if Patient.objects.filter(pk=slug).exists():
            patient = Patient.objects.get(pk=slug)
            form_instance = EditPatientForm(instance=patient)
            return render(request, 
                self.update_template,
                {'form': form_instance})

        # Render New Patient Form
        form = PatientForm()
        user_creation = RegisterForm()
        return render(request, 
            self.create_template,
            {'form': form, 'user_creation':user_creation})
    
    def post(self, request, slug):
        # Updating Patient's Record
        if Patient.objects.filter(pk=slug).exists():
            patient = Patient.objects.get(pk=slug)
            form = EditPatientForm(request.POST, instance=patient)
            if form.is_valid():
                form.save()
                messages.success(request, "Patient Record Updated Successfully")
                return redirect('edit-patient', slug)
            messages.error(request, form.errors)
            return redirect('edit-patient', slug)
        
        # Saving New Patient's Record
        new_form = PatientForm(request.POST)
        if new_form.is_valid():
            new_form.save()
            return redirect('patients')
        return redirect('create-patient')


class ListDrugView(LoginRequiredMixin, View):
    template_name = 'core/drugs/view-drug.html'

    def get(self, request):
        drugs = DrugInventory.objects.all()
        return render(request,
            self.template_name,
            {'drugs': drugs})

class createDrugView(LoginRequiredMixin, View):
    template_name = 'core/drugs/create-drug.html'
    edit_drug_template = 'core/drugs/edit-drug.html'

    def get(self, request, slug=None):
        if slug != None:
            drug = DrugInventory.objects.get(pk=slug)
            form = DrugInventoryForm(instance=drug)
            return render(request,
                        self.edit_drug_template,
                        {'form':form, 'drug':drug})
        form = DrugInventoryForm()
        return render(request, 
            self.template_name,
            {'form': form})
    
    def post(self, request, slug=None):
        if slug != None:
            drug = DrugInventory.objects.get(pk=slug)
            form = DrugInventoryForm(request.POST, instance=drug)
            if form.is_valid():
                form.save()
                messages.success(request, "Drug Updated Successfully")
                return redirect('list-drugs')
        else:
            form = DrugInventoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Drug Created Successfully")
                return redirect('list-drugs')

        messages.error(request, form.errors)
        return redirect('create-drug')
    
class DeleteDrug(View):
    def get(self, request, slug):
        DrugInventory.objects.get(pk=slug).delete()
        messages.success(request, "Drug Deleted Successfully")
        return redirect('list-drugs')