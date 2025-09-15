from rest_framework import serializers
from .models import Appointment, MedicalNote


class AppointmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Appointment
    fields = [
      "id",
      "patient",
      "doctor",
      "appointment_date",
      "appointment_time",
      "notes",
      "status",
    ]


class MedicalNoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = MedicalNote
    fields = ["id", "appointment", "note", "date"]
