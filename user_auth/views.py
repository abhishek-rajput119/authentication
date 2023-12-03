from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers.user_serializer import UserSerializer
from rest_framework import status
from .controllers.user_controller import UserController
from .permissions import IsAuthenticated


class UserRegistrationView(APIView):
    def post(self, request):
        serialized_data = UserSerializer(data=request.data)
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


class UserLoginView(APIView):
    def post(self, request):
        request_data = request.data

        if not request_data.get("username") or not request_data.get("password"):
            return Response({"message": "Details Missing"}, status=status.HTTP_400_BAD_REQUEST)

        user_details, message = UserController().login_user(request_data.get("username"), request_data.get("password"))

        if user_details:
            response = {
                "User details": user_details,
                "token": message
            }

            return Response(response, status=status.HTTP_200_OK)

        return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        username = request.user.get("username")

        user_instance, error = UserController().get_user_by_username(username)
        if error:
            return Response({"message": error}, status=status.HTTP_404_NOT_FOUND)
        response = UserSerializer(user_instance).data
        return Response(response, status=status.HTTP_200_OK)

class UserUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request):
        username = request.user.get("username")
        user_instance, error = UserController().get_user_by_username(username)
        if error:
            return Response({"message": error}, status=status.HTTP_404_NOT_FOUND)
        updated_user, error = UserController().update_user_details(user_instance, request.data)

        if error:
            return Response({"message": error}, status=status.HTTP_400_BAD_REQUEST)
        response = {
            "message": "Successfully Updated.",
            "details": UserSerializer(updated_user).data
        }
        return Response(response, status=status.HTTP_200_OK)

class UserDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        username = request.user.get("username")
        password = request.data.get("password")
        user_instance, error = UserController().get_user_by_username(username)
        if error:
            return Response({"message": error}, status=status.HTTP_404_NOT_FOUND)

        user, message = UserController().delete_user_using_password_confirmation(user_instance, password)
        response = {"message": message}

        if not user:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(response, status=status.HTTP_204_NO_CONTENT)

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        username = request.user.get('username')
        access_token = request.headers.get('Authorization')
        result = UserController().logout_user(username, access_token)

        if result:
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)

        return Response({"message": "Can't complete request"}, status=status.HTTP_400_BAD_REQUEST)
