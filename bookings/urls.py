from .viewsets import AppointmentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"appointments", AppointmentViewSet, basename="appointment")

urlpatterns = router.urls
