from .serializers import PatientSerializer
from .models import Patient

# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

"""
GET /patients/
POST /patients/
PUT /patients/<int:pk>/
DELETE /patients/<int:pk>/

VISTAS BASADAS EN FUNCIONES USAN @api_view()
VISTAS BASADAS EN CLASES USAN APIView() y en la urls se usa el .as_view()

"""


class PatientListView(APIView):
  allowed_methods = ["GET", "POST"]

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


# @api_view(["GET", "POST"])
# def list_patients(request):
#   if request.method == "GET":
#     patients = Patient.objects.all()
#     serializer = PatientSerializer(patients, many=True)
#     return Response(serializer.data)
#   elif request.method == "POST":
#     # aquí no necesito una query que me traiga todos los pacientes, solo necesito crear uno
#     serializer = PatientSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientDetailView(APIView):
  allowed_methods = ["GET", "PUT", "DELETE"]

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


# @api_view(["GET", "PUT", "DELETE"])
# def update_patient(request, pk):
#   patient = get_object_or_404(Patient, id=pk)

#   if request.method == "GET":
#     serializer = PatientSerializer(patient)
#     return Response(serializer.data, status=status.HTTP_200_OK)

#   elif request.method == "PUT":
#     serializer = PatientSerializer(patient, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   elif request.method == "DELETE":
#     patient.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
