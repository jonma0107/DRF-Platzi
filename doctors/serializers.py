from rest_framework import serializers
from .models import Doctor, Department, DoctorAvailability, MedicalNote


class DoctorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Doctor
    fields = [
      "id",
      "first_name",
      "last_name",
      "qualification",
      "contact_number",
      "email",
      "address",
      "biography",
    ]


class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields = ["id", "name", "description"]


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
  class Meta:
    model = DoctorAvailability
    fields = [
      "id",
      "doctor",
      "start_date",
      "end_date",
      "start_time",
      "end_time",
    ]


class MedicalNoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = MedicalNote
    fields = ["id", "doctor", "note", "date"]
