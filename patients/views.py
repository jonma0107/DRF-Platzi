from .serializers import PatientSerializer
from .models import Patient

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
