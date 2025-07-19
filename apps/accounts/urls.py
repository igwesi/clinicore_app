from django.urls import path
from .views import *


urlpatterns = [
    path('auth/', authView, name="auth-signin"),
    path('auth/role/', AuthRoleSelection.as_view(), name='auth-role-selection'),
    path('auth/profile/', AuthProfileSetup.as_view(), name='auth-profile-setup'),
    path('dashboard/', dashboardView.as_view(), name='dashboard'),
    path('login/', loginView.as_view(), name='login'),
    path('register/', registerView.as_view(), name='register'),
    path('logout/', logoutView.as_view(), name='logout'),
]