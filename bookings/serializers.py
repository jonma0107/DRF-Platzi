from rest_framework import serializers
from .models import Appointment, MedicalNote
from patients.models import Patient
from doctors.models import Doctor


class AppointmentSerializer(serializers.ModelSerializer):
  patient = serializers.StringRelatedField(read_only=True)
  doctor = serializers.StringRelatedField(read_only=True)
  patient_id = serializers.PrimaryKeyRelatedField(
    source="patient", queryset=Patient.objects.all(), write_only=True
  )
  doctor_id = serializers.PrimaryKeyRelatedField(
    source="doctor", queryset=Doctor.objects.all(), write_only=True
  )

  class Meta:
    model = Appointment
    fields = [
      "id",
      "patient_id",  # no edita porque solo se selecciona la relación con el paciente
      "doctor_id",  # no edita porque solo se selecciona la relación con el doctor
      "patient",  # solo lectura
      "doctor",  # solo lectura
      "appointment_date",
      "appointment_time",
      "notes",
      "status",
    ]


class MedicalNoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = MedicalNote
    fields = ["id", "appointment", "note", "date"]
