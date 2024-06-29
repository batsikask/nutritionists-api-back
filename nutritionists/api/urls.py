from django.urls import path
from nutritionists.api.views import *
urlpatterns = [
    path("nutritionists/", NutritionistListAPIView.as_view(), name="nutritionist_list"),
    path("nutritionists/<int:pk>", NutritionistDetailAPIView.as_view(), name="nutritionist_detail"),
    path("nutritionists/<int:nutritionist_pk>/clients/", NutritionistClientListCreateAPIView.as_view(), name="nutritionist_client_list"),
    path("nutritionists/<int:nutritionist_pk>/clients/<int:client_pk>", NutritionistClientDetailAPIView.as_view(), name="nutritionist_client_detail"),
    path("nutritionists/<int:nutritionist_pk>/clients/<int:client_pk>/linkto/users/<int:user_pk>", UserToClientLinkAPIView.as_view(), name="nutritionist_client_user_link"),
]