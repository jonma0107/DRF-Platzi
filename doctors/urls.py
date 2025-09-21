from django.urls import path
from .views import list_doctors, doctor_detail

urlpatterns = [
  path("doctors/", list_doctors, name="list_doctors"),
  path("doctors/<int:pk>/", doctor_detail, name="doctor_detail"),
]
