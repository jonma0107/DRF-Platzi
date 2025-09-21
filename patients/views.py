from .serializers import PatientSerializer
from .models import Patient

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

"""
GET /patients/
POST /patients/
PUT /patients/update/<int:pk>/
DELETE /patients/update/<int:pk>/

VISTAS BASADAS EN FUNCIONES USAN @api_view()
"""


@api_view(["GET", "POST"])
def list_patients(request):
  if request.method == "GET":
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)
  elif request.method == "POST":
    # aquí no necesito una query que me traiga todos los pacientes, solo necesito crear uno
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT", "DELETE"])
def update_patient(request, pk):
  patient = get_object_or_404(Patient, id=pk)

  if request.method == "PUT":
    serializer = PatientSerializer(patient, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == "DELETE":
    patient.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
