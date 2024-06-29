from rest_framework import permissions
from nutritionists.models import Nutritionist
from rest_framework.generics import get_object_or_404
from users.models import NormalUser


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object instance to access it.
    """
    def has_permission(self, request, view):
        user_pk = view.kwargs['user_pk']
        normal_user = get_object_or_404(NormalUser, pk=user_pk)
        return request.user.id == normal_user.user.id
    
    def has_object_permission(self, request, view, obj):
        user_pk = view.kwargs['user_pk']
        normal_user = get_object_or_404(NormalUser, pk=user_pk)
        return obj.user.id == normal_user.id
    
class IsNutritionistClientOwner(permissions.BasePermission):
    """
    Custom permission to allow a nutritionist to only access their own clients' measurements.
    """
    def has_permission(self, request, view):
        nutritionist_pk = view.kwargs['nutritionist_pk']
        nutritionist = get_object_or_404(Nutritionist, pk=nutritionist_pk)
        return nutritionist.user == request.user       
    
    def has_object_permission(self, request, view, obj):
        nutritionist_pk = view.kwargs['nutritionist_pk']
        nutritionist = get_object_or_404(Nutritionist, pk=nutritionist_pk)
        return obj.client in nutritionist.clients.all()