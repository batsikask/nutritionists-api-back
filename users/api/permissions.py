from rest_framework import permissions
    
class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object instance to access it.
    """
    def has_object_permission(self, request, view, obj):
        if (obj.__class__.__name__ == 'NormalUser'):
            return obj.user.id == request.user.id
        else:
            return obj.id == request.user.id