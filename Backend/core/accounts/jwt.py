import jwt
from datetime import datetime, timedelta, timezone
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import BasePermission


class JWTService:
    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            
            user_id = payload.get("user_id")
            
            if not user_id:
                raise AuthenticationFailed("User Id is required")
        
            user = User.objects.filter(id=user_id).first()
            
            if not user:
                raise AuthenticationFailed('User does not exist')
        
            payload['username'] = user.username  

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token")

    @staticmethod
    def get_jwt_token(request):
        token = request.headers.get("Authorization")
        if not token or not token.startswith("Bearer "):
            raise AuthenticationFailed("Authorization header missing or invalid")
        return token.split(" ")[1]

    @staticmethod
    def validate_user_from_token(payload):
        user_id = payload.get("user_id")
        username = payload.get("username")

        if not (user_id and username):
            raise AuthenticationFailed("Incomplete token payload")

        user = User.objects.filter(id=user_id, username=username).first()
        
        if not user:
            raise AuthenticationFailed("Invalid User")

        return user


class IsValidUser(BasePermission):

    def has_permission(self, request, view):
        try:
            token = JWTService.get_jwt_token(request)
            payload = JWTService.decode_token(token)

            user = JWTService.validate_user_from_token(payload)

            request.user = user
            
            return True

        except AuthenticationFailed as e:
            raise AuthenticationFailed(f"Permission denied: {str(e)}")
