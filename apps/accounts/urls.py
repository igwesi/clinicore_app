from django.urls import path
from .views import *


urlpatterns = [
    path('', dashboardView.as_view(), name='dashboard'),
    path('login/', loginView.as_view(), name='login'),
    path('register/', registerView.as_view(), name='register'),
    # path('logout/', logoutView.as_view(), name='logout'),
    # path('password_reset/', passwordResetView.as_view(), name='password_reset'),
    # path('password_change/', passwordChangeView.as_view(), name='password_change'),
]