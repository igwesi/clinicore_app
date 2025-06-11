from django.shortcuts import render
from django.views import View


class clinicView(View):
    def get(self, request):
        return render(request, 'index.html')