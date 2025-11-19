from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer, ProfileSerializer, ChangePasswordSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """
    POST /api/auth/register/
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class ProfileView(generics.RetrieveUpdateAPIView):
    """
    GET /api/auth/profile/       -> get current user's profile
    PATCH /api/auth/profile/     -> update profile fields (first_name, last_name, email)
    """
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class ChangePasswordView(APIView):
    """
    POST /api/auth/change-password/
    Body: {"old_password": "...", "new_password": "..."}
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        old = serializer.validated_data["old_password"]
        new = serializer.validated_data["new_password"]

        if not user.check_password(old):
            return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new)
        user.save()
        return Response({"detail": "Password changed successfully."}, status=status.HTTP_200_OK)
