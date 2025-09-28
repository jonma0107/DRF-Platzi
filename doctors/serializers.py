from rest_framework import serializers
from .models import Doctor, Department, DoctorAvailability, MedicalNote
from bookings.serializers import AppointmentSerializer


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
  time_worked = serializers.SerializerMethodField()

  class Meta:
    model = DoctorAvailability
    fields = [
      "id",
      "doctor",
      "start_date",
      "end_date",
      "start_time",
      "end_time",
      "time_worked",
    ]

  def get_time_worked(self, obj):
    time_worked = obj.end_date - obj.start_date
    return f"{time_worked.days} días"


class DoctorSerializer(serializers.ModelSerializer):
  appointments = AppointmentSerializer(many=True, read_only=True)
  # experience = DoctorAvailabilitySerializer( source="availabilities", many=True, read_only=True)
  time_experience = serializers.SerializerMethodField()

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
      "appointments",
      # "experience",
      "time_experience",
    ]

  def get_time_experience(self, obj):
    availabilities = obj.availabilities.all()

    if not availabilities.exists():
      return "Sin experiencia registrada"

    # Calcular el tiempo total sumando todos los períodos
    total_days = 0
    for availability in availabilities:
      time_worked = availability.end_date - availability.start_date
      total_days += time_worked.days
      total_months = total_days // 30
      total_years = total_months // 12

    return f"{total_years} años, {total_months % 12} meses, {total_days % 30} días de experiencia total"


class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields = ["id", "name", "description"]


class MedicalNoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = MedicalNote
    fields = ["id", "doctor", "note", "date"]
