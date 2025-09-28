from django.test import TestCase
from django.contrib.auth.models import User, Group
from patients.models import Patient
from doctors.models import Doctor
from rest_framework.test import APIClient
from datetime import date
from django.urls import reverse


class DoctorTestCase(TestCase):
  def setUp(self):
    # Crear usuario
    self.user = User.objects.create_user(
      username="testuser", password="testpass123"
    )

    # Crear grupo de administradores
    self.admin_group = Group.objects.create(name="administradores")
    self.user.groups.add(self.admin_group)

    self.patient = Patient.objects.create(
      first_name="John",
      last_name="Doe",
      email="john.doe@example.com",
      contact_number="1234567890",
      date_of_birth=date(2005, 1, 1),
      address="123 Main St, Anytown, USA",
      medical_history="No medical history",
    )
    self.doctor = Doctor.objects.create(
      first_name="Jane",
      last_name="Smith",
      email="jane.smith@example.com",
      contact_number="1234567890",
      address="123 Main St, Anytown, USA",
      qualification="MD",
      biography="Dr. Smith is a general practitioner with 10 years of experience.",
    )
    self.client = APIClient()
    # Autenticar al usuario
    self.client.force_authenticate(user=self.user)

  def test_patient_creation(self):
    self.assertEqual(self.patient.first_name, "John")

  def test_doctor_creation(self):
    self.assertEqual(self.doctor.first_name, "Jane")

  def test_patient_list(self):
    url = reverse("patients-list")
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.data), 1)  # Verificar que hay un paciente
    self.assertEqual(response.data[0]["first_name"], "John")

  def test_doctor_list(self):
    url = reverse("doctors-list")
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.data), 1)  # Verificar que hay un doctor
    self.assertEqual(response.data[0]["first_name"], "Jane")
