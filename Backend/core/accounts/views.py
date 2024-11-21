from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User


class SignUpViewSet(ViewSet):
    def post(self, request):
        print(request.data)
        username = request.data.get("username")
        password = request.data.get("password")
        if User.objects.filter(username=username).exists():
            raise ValidationError("User with this username already exists.")

        user = User.objects.create_user(username=username, password=password)
        return Response(
            {"message": "User created successfully"}, status=status.HTTP_201_CREATED
        )
