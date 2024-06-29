from rest_framework import permissions
from nutritionists.models import Nutritionist
from rest_framework.generics import get_object_or_404

class IsNutritionistOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a nutritionist instance to access it.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='Nutritionist').exists()

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    
class IsNutritionistClientOwner(permissions.BasePermission):
    """
    Custom permission to allow a nutritionist to only access their own clients.
    """
    def has_permission(self, request, view):
        nutritionist_pk = view.kwargs['nutritionist_pk']
        nutritionist = get_object_or_404(Nutritionist, pk=nutritionist_pk)
        return nutritionist.user == request.user       
    
    def has_object_permission(self, request, view, obj):
        nutritionist_pk = view.kwargs['nutritionist_pk']
        nutritionist = get_object_or_404(Nutritionist, pk=nutritionist_pk)
        return obj in nutritionist.clients.all()