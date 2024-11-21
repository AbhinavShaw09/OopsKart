from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.generics import ListAPIView

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self,serializer):
        serializer.save()

    def create_product(self, request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs) -> Response:
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data) 
    
    def list(self,request)-> Response:
        return Response(self.queryset)
