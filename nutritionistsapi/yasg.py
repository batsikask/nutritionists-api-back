from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Nutritionists API",
      default_version='v1',
      description="API for Nutritionists and client management",
      terms_of_service="",
      contact=openapi.Contact(email=""),
      license=openapi.License(name=""),
   ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)