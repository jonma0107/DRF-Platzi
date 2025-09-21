from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Doctor
from .serializers import DoctorSerializer

from django.shortcuts import get_object_or_404


@api_view(["GET", "POST"])
def list_doctors(request):
  if request.method == "GET":
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == "POST":
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def doctor_detail(request, pk):
  doctor = get_object_or_404(Doctor, pk=pk)

  if request.method == "GET":
    serializer = DoctorSerializer(doctor)
    return Response(serializer.data, status=status.HTTP_200_OK)

  elif request.method == "PUT":
    serializer = DoctorSerializer(doctor, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == "DELETE":
    doctor.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
