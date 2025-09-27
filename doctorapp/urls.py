"""
URL configuration for doctorapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# from rest_framework import permissions
# from rest_framework.authentication import SessionAuthentication
# from rest_framework_simplejwt.authentication import JWTAuthentication
from doctorapp.utils.schema_generator import DoctorappSchemaGenerator

schema_view_authenticated = get_schema_view(
  openapi.Info(
    title="API Documentation",
    default_version="v1",
    description="Documentation for API.",
  ),
  public=True,
  #   permission_classes=[permissions.IsAuthenticated],
  #   authentication_classes=[JWTAuthentication, SessionAuthentication],
  generator_class=DoctorappSchemaGenerator,
)

urlpatterns = [
  path("admin/", admin.site.urls),
  path(
    "api/auth/", include("rest_framework.urls")
  ),  # para que se pueda autenticar con el login de django
  path("api/patients/", include("patients.urls")),
  path("api/doctors/", include("doctors.urls")),
  path("api/bookings/", include("bookings.urls")),
  # Swagger
  path(
    "swagger/",
    schema_view_authenticated.with_ui("swagger", cache_timeout=0),
    name="schema-swagger-ui",
  ),
  path(
    "redoc/",
    schema_view_authenticated.with_ui("redoc", cache_timeout=0),
    name="schema-redoc",
  ),
  re_path(
    r"^swagger(?P<format>\.json|\.yaml)$",
    schema_view_authenticated.without_ui(cache_timeout=0),
    name="schema-json-authenticated",
  ),
]
