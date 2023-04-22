from rest_framework.permissions import BasePermission

class OnePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return False
        else:
            return True
