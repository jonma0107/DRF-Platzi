from django.urls import path

# from .views import list_patients, update_patient
from .views import PatientListView, PatientDetailView, PatientAppointmentView

urlpatterns = [
  # path("patients/", list_patients),
  path("patients/", PatientListView.as_view()),
  # path("patients/update/<int:pk>/", update_patient),
  path("patients/<int:pk>/", PatientDetailView.as_view()),
  path("patients/<int:pk>/appointments/", PatientAppointmentView.as_view()),
  path(
    "patients/<int:pk>/appointments/<int:appointment_id>/",
    PatientAppointmentView.as_view(),
  ),
]
