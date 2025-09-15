from rest_framework import serializers
from .models import Patient, Insurance, MedicalRecord


class PatientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Patient
    fields = [
      "id",
      "first_name",
      "last_name",
      "date_of_birth",
      "contact_number",
      "email",
      "address",
      "medical_history",
    ]


class InsuranceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Insurance
    fields = ["id", "patient", "provider", "policy_number", "expiration_date"]


class MedicalRecordSerializer(serializers.ModelSerializer):
  class Meta:
    model = MedicalRecord
    fields = [
      "id",
      "patient",
      "date",
      "diagnosis",
      "treatment",
      "follow_up_date",
    ]
