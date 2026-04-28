from django.urls import path
from .views import (
    RegisterView,
    LogoutView,
    ProfileView,
    ChangePasswordView,
    DeleteAccountView,
)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("api/register/", RegisterView.as_view()),
    path("api/login/", TokenObtainPairView.as_view()),
    path("api/logout/", LogoutView.as_view()),
    path("api/profile/<int:pk>/", ProfileView.as_view()),
    path("api/changepassword/<int:pk>/", ChangePasswordView.as_view()),
    path("api/deleteaccount/<int:pk>/", DeleteAccountView.as_view()),
]
