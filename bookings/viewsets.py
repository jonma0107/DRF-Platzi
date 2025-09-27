from rest_framework.viewsets import ModelViewSet
from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class AppointmentViewSet(ModelViewSet):
  queryset = Appointment.objects.all()
  serializer_class = AppointmentSerializer
  permission_classes = [IsAuthenticated]

  @action(
    ["GET"], detail=True, url_path="medical-history"
  )  # Funciona solo con viewsets
  def get_medical_history(self, request, pk):
    appointment = self.get_object()
    serializer = AppointmentSerializer(appointment)
    return Response(serializer.data, status=status.HTTP_200_OK)
