from django.urls import path
from .views import *


urlpatterns = [
    path('auth/', authView, name="auth-signin"),
    path('dashboard/', dashboardView.as_view(), name='dashboard'),
    path('login/', loginView.as_view(), name='login'),
    path('register/', registerView.as_view(), name='register'),
    path('logout/', logoutView.as_view(), name='logout'),
]