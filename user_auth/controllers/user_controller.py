from user_auth.models import UserDetails
from user_auth.constants.constants import Constants
from user_auth.utils.jwt_util import Auth
from user_auth.utils.hashing import PasswordHasher


class UserController:
    def __init__(self):
        pass

    def register_user(self, user_data: dict):
        username = user_data.get("username")
        user = UserDetails.objects.filter(username=username)

        if user:
            return None, {"username": Constants.UserConstants.ALREADY_EXISTS}

        try:
            salt, hashed_password = PasswordHasher().hash_password_with_new_salt(user_data.get("password"))
            user_data.update({"password": hashed_password.decode('utf-8'), 'salt': salt.decode('utf-8')})
            UserDetails.objects.create(**user_data)
        except Exception as e:
            return None, {"error": f"{e}"}

        user_details = self.get_user_details(user_data)
        return user_details, None

    def login_user(self, payload):
        if not payload or not payload.get("username"):
            return None, {"message": "username is required"}
        if not payload.get("password"):
            return None, {"message": "password is required"}

        token = Auth.generate_jwt_token(payload)
        if token:
            return {"token": token}

        return {"message": "cannot get the token"}

    def get_user_details(self, user_data):
        user_details = dict()

        user_details["name"] = user_data.get("name")
        user_details["username"] = user_data.get("username")
        user_details["bio"] = user_data.get("bio")
        user_details["age"] = user_data.get("age")

        return user_details
