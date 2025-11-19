# accounts/urls.py
from django.urls import path
from .views import RegisterView, ProfileView, ChangePasswordView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="auth_register"),
    path("profile/", ProfileView.as_view(), name="auth_profile"),
    path("change-password/", ChangePasswordView.as_view(), name="auth_change_password"),
]
