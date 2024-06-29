from django.urls import path
from measurements.api.views import *

urlpatterns = [
    # User related urls
    path("users/<int:user_pk>/measurements/", AllUserMeasurementsView.as_view(), name="all_measurements_list"),
    path("users/<int:user_pk>/measurements/body/", BodyMeasurementListCreateAPIView.as_view(), name="body_measurement_list"),
    path("users/<int:user_pk>/measurements/body/<int:pk>", BodyMeasurementDetailAPIView.as_view(), name="body_measurement_detail"),
    path("users/<int:user_pk>/measurements/segmental/", SegmentalBodyMeasurementListCreateAPIView.as_view(), name="segmental_measurement_list"),
    path("users/<int:user_pk>/measurements/segmental/<int:pk>", SegmentalBodyMeasurementDetailAPIView.as_view(), name="segmental_measurement_detail"),
    path("users/<int:user_pk>/measurements/biochemical/", BiochemicalMeasurementListCreateAPIView.as_view(), name="biochemical_measurement_list"),
    path("users/<int:user_pk>/measurements/biochemical/<int:pk>", BiochemicalMeasurementDetailAPIView.as_view(), name="biochemical_measurement_detail"),
    path("users/<int:user_pk>/measurements/disease/", DiseasesListCreateAPIView.as_view(), name="diseases_list"),
    path("users/<int:user_pk>/measurements/disease/<int:pk>", DiseasesDetailAPIView.as_view(), name="diseases_detail"),
    path("users/<int:user_pk>/measurements/diet/", DietListCreateAPIView.as_view(), name="diet_list"),
    path("users/<int:user_pk>/measurements/diet/<int:pk>", DietDetailAPIView.as_view(), name="diet_detail"),

    # Nutritionist with client related urls
    path("nutritionists/<int:nutritionist_pk>/clients/<int:client_pk>/measurements/", AllClientMeasurementsView.as_view(), name="all_client_measurements_list"),
    path("nutritionists/<int:nutritionist_pk>/clients/<int:client_pk>/measurements/body/", BodyMeasurementListCreateAPIView.as_view(), name="client_body_measurement_list"),
    path("nutritionists/<int:nutritionist_pk>/clients/<int:client_pk>/measurements/body/<int:pk>", BodyMeasurementDetailAPIView.as_view(), name="client_body_measurement_detail"),
    path("nutritionists/<int:nutritionist_pk>/clients/<int:client_pk>/measurements/segmental/", SegmentalBodyMeasurementListCreateAPIView.as_view(), name="client_segmental_measurement_list"),
    path("nutritionists/<int:nutritionist_pk>/clients/<int:client_pk>/measurements/segmental/<int:pk>", SegmentalBodyMeasurementDetailAPIView.as_view(), name="client_segmental_measurement_detail"),
    path("nutritionists/<int:nutritionist_pk>/clients/<int:client_pk>/measurements/biochemical/", BiochemicalMeasurementListCreateAPIView.as_view(), name="client_biochemical_measurement_list"),
    path("nutritionists/<int:nutritionist_pk>/clients/<int:client_pk>/measurements/biochemical/<int:pk>", BiochemicalMeasurementDetailAPIView.as_view(), name="client_biochemical_measurement_detail"),
    path("nutritionists/<int:nutritionist_pk>/clients/<int:client_pk>/measurements/disease/", DiseasesListCreateAPIView.as_view(), name="client_diseases_list"),
    path("nutritionists/<int:nutritionist_pk>/clients/<int:client_pk>/measurements/disease/<int:pk>", DiseasesDetailAPIView.as_view(), name="client_diseases_detail"),
    path("nutritionists/<int:nutritionist_pk>/clients/<int:client_pk>/measurements/diet/", DietListCreateAPIView.as_view(), name="client_diet_list"),
    path("nutritionists/<int:nutritionist_pk>/clients/<int:client_pk>/measurements/diet/<int:pk>", DietDetailAPIView.as_view(), name="client_diet_detail"),

]
