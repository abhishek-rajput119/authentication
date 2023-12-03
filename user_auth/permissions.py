from rest_framework import exceptions, status
from rest_framework.permissions import BasePermission
from user_auth.models import BlockedToken
from user_auth.utils.jwt_util import Auth


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        access_token = request.headers.get('Authorization')
        payload, error_message = Auth().authorize(access_token)
        if not payload:
            raise exceptions.PermissionDenied(detail={"message": error_message}, code=status.HTTP_401_UNAUTHORIZED)

        request.user = payload

        blocked = BlockedToken.objects.filter(username=payload.get("username"), token=access_token).exists()

        return not blocked
