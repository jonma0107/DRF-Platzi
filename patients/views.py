from .serializers import PatientSerializer
from .models import Patient
from bookings.models import Appointment
from bookings.serializers import AppointmentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .permissions import IsAdminOrReadOnly

"""
GET /patients/
POST /patients/
PUT /patients/<int:pk>/
DELETE /patients/<int:pk>/
GET /patients/<int:pk>/appointments/
POST /patients/<int:pk>/appointments/
PUT /patients/<int:pk>/appointments/<int:appointment_id>/
DELETE /patients/<int:pk>/appointments/<int:appointment_id>/

VISTAS BASADAS EN CLASES USAN APIView() y en la urls se usa el .as_view()

"""


class PatientListView(APIView):
  allowed_methods = ["GET", "POST"]
  permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

  def get(self, request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientDetailView(APIView):
  allowed_methods = ["GET", "PUT", "DELETE"]
  permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

  def get(self, request, pk):
    patient = get_object_or_404(Patient, id=pk)

    serializer = PatientSerializer(patient)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def put(self, request, pk):
    patient = get_object_or_404(Patient, id=pk)
    serializer = PatientSerializer(patient, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    patient = get_object_or_404(Patient, id=pk)
    patient.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class PatientAppointmentView(APIView):
  """Vista para crear y obtener agendamientos de un paciente específico"""

  permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

  def get(self, request, pk, appointment_id=None):
    """Obtener todos los agendamientos del paciente o un agendamiento específico"""
    patient = get_object_or_404(Patient, id=pk)

    if appointment_id:
      # Obtener un agendamiento específico
      appointment = get_object_or_404(
        Appointment, id=appointment_id, patient=patient
      )
      serializer = AppointmentSerializer(appointment)
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      # Obtener todos los agendamientos del paciente
      appointments = Appointment.objects.filter(patient=patient)
      serializer = AppointmentSerializer(appointments, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request, pk, appointment_id=None):
    """Crear un nuevo agendamiento para el paciente"""

    # Agregar el patient_id a los datos del request
    appointment_data = request.data.copy()
    appointment_data["patient_id"] = pk

    # Crear el agendamiento
    serializer = AppointmentSerializer(data=appointment_data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk, appointment_id):
    """Actualizar un agendamiento específico del paciente"""
    # Verificar que el paciente existe
    patient = get_object_or_404(Patient, id=pk)

    # Verificar que el agendamiento existe y pertenece al paciente
    appointment = get_object_or_404(
      Appointment, id=appointment_id, patient=patient
    )

    # Agregar el patient_id a los datos del request
    appointment_data = request.data.copy()
    appointment_data["patient_id"] = pk

    # Actualizar el agendamiento
    serializer = AppointmentSerializer(appointment, data=appointment_data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, appointment_id):
    """Eliminar un agendamiento específico del paciente"""
    # Verificar que el paciente existe
    patient = get_object_or_404(Patient, id=pk)

    # Verificar que el agendamiento existe y pertenece al paciente
    appointment = get_object_or_404(
      Appointment, id=appointment_id, patient=patient
    )

    # Eliminar el agendamiento
    appointment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
