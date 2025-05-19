from django.urls import path
from .views import (
    clinicView,
)

urlpatterns = [
    path('', clinicView.as_view(), name='home'),
]