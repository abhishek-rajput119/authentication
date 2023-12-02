from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers.user_serializer import RegistrationSerializer
from rest_framework import status
from .controllers.user_controller import UserController


class UserView(APIView):
    def post(self, request):
        serialized_data = RegistrationSerializer(data=request.data)
        if serialized_data.is_valid():
            user_details, error = UserController().register_user(serialized_data.validated_data)

            if error:
                return Response({"message": error}, status=status.HTTP_400_BAD_REQUEST)
            response = {
                "message": "Account Successfully created.",
                "details": user_details
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response({"message": serialized_data.errors}, status=status.HTTP_400_BAD_REQUEST)
