from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    RegisterSerializer,
    UserProfileSerializer,
)


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class LogoutView(APIView):
    def post(self, request):
        return Response("Logged out")


class ProfileView(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ChangePasswordView(APIView):
    def post(self, request):
        user = User.objects.get(pk=request.data["id"])
        user.password = request.data["new_password"]
        user.save()
        return Response("Password changed")


class DeleteAccountView(APIView):
    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response("Deleted")
