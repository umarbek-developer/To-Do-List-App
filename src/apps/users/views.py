from rest_framework.views import APIView
from rest_framework.response import Response
from apps.users.models import User
from .serializers import UserSerializer
from rest_framework import status


class LoginView(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = User.objects.filter(username=username)

        if user.exists():
            user = user.first()
            print(user.password)
            if user.check_password(password):
                user_data = UserSerializer(user)
                return Response({"message": "Login Success", "user": user_data.data})

        return Response(
            {"message": "Kapitan Eshitadi"}, status=status.HTTP_400_BAD_REQUEST
        )
