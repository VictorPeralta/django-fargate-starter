from django.shortcuts import render
from rest_framework import views
from rest_framework import generics, status
from rest_framework.response import Response

from apps.users.serializers import LoginSerializer
from django.contrib.auth import login, logout

# Create your views here.


class LoginView(generics.GenericAPIView):
    """Use this endpoint to obtain user authentication token."""

    serializer_class = LoginSerializer

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login(request, serializer.user)
        return Response(status=status.HTTP_200_OK)

class LogoutView(views.APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
