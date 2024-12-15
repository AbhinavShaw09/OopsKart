import re

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError as DjangoValidationError



class SignUpViewSet(ViewSet):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # Check if the username and password are provided
        if not username or not password:
            raise ValidationError("Username and password are required.")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            raise ValidationError("User with this username already exists.")

        # Optionally, validate the password strength (e.g., minimum length)
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r"\d", password):
            raise ValidationError("Password must contain at least one digit.")
        if not re.search(r"[A-Za-z]", password):
            raise ValidationError("Password must contain at least one letter.")

        # Create the user
        try:
            user = User.objects.create_user(username=username, password=password)
        except DjangoValidationError as e:
            raise ValidationError(f"Error creating user: {str(e)}")

        # Optionally, create a token for the user (if you want to auto-login after signup)
        refresh = RefreshToken.for_user(user)
        
        return Response(
            {
                "message": "User created successfully",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            },
            status=status.HTTP_201_CREATED,
        )



class LoginView(ViewSet):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            raise AuthenticationFailed("Username and password are required")

        user = authenticate(username=username, password=password)

        if not user:
            raise AuthenticationFailed("Invalid credentials")

        refresh = RefreshToken.for_user(user)

        return Response({"refresh": str(refresh), "access": str(refresh.access_token)})
