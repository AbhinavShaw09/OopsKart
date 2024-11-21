from django.urls import path
from .views import SignUpViewSet

urlpatterns = [
    path("signup/", SignUpViewSet.as_view({"post": "post"}), name="signup"),
]
