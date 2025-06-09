from django.urls import path
from .views import *


urlpatterns = [
    path('', staffDashboard.as_view(), name='staff-dashboard'),
    path('login/', staffLogin.as_view(), name='staff-login'),
]