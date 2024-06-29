from rest_framework import generics
from users.models import CustomUser, NormalUser
from users.api.serializers import CustomUserSerializer, NormalUserSerializer, CustomUserRegisterSerializer
from dj_rest_auth.registration.views import RegisterView
from users.api.permissions import IsOwner
from rest_framework.permissions import IsAdminUser, AllowAny

class CustomUserRegisterView(RegisterView):
    """
    Custom RegisterView that overrides the default RegisterSerializer of dj_rest_auth with CustomUserRegisterSerializer.
    """
    serializer_class = CustomUserRegisterSerializer
    permission_classes = [AllowAny]

class CustomUserListAPIView(generics.ListAPIView):
    """
    Standard ListAPIView for CustomUser model accessible only for staff users.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]

class CustomUserCreateAPIView(generics.CreateAPIView):
    """
    Standard CreateAPIView for CustomUser model accessible only for staff users.
    This doesn't go through the standard dj_rest_auth registration process.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]
    
class CustomUserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Standard RetrieveAPIView for CustomUser model accessible for staff users and object owners.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwner or IsAdminUser]

class NormalUserListAPIView(generics.ListAPIView):
    """
    Standard ListAPIView for NormalUser model accessible only for staff users.
    """
    queryset = NormalUser.objects.all()
    serializer_class = NormalUserSerializer
    permission_classes = [IsAdminUser]

class NormalUserDetailAPIView(generics.RetrieveUpdateAPIView):
    """
    Standard RetrieveUpdateAPIView for NormalUser model accessible for staff users and object owners.
    Delete method is not implemented as it is handled by CASCADE during the deletion of the related CustomUser.
    """
    queryset = NormalUser.objects.all()
    serializer_class = NormalUserSerializer
    permission_classes = [IsOwner or IsAdminUser]