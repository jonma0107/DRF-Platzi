from django.urls import path
from .views import list_patients, update_patient

urlpatterns = [
  path("patients/", list_patients),
  path("patients/update/<int:pk>/", update_patient),
]
