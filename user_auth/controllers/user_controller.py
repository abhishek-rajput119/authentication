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

    def login_user(self, username, password):
        if not username:
            return None, {"message": "username is required"}
        if not password:
            return None, {"message": "password is required"}

        try:
            user = UserDetails.objects.filter(username=username).first()
            if not user:
                return None, Constants.UserConstants.DOES_NOT_EXISTS
            password_salt = bytes(user.salt, 'utf-8')

            hashed_password = PasswordHasher().hash_password(password, password_salt)
            hashed_password = hashed_password.decode('utf-8')
            user = UserDetails.objects.filter(username=username, password=hashed_password).first()
            if not user:
                return None, Constants.UserConstants.INCORRECT_CREDENTIALS

            user_details = {
                "name": user.name,
                "username": user.username,
                "bio": user.bio,
                "age": user.age,
            }

            jwt_token = Auth().generate_jwt_token(
                {"name": user_details.get("name"), "username": user_details.get("username")})
            if jwt_token:
                return user_details, jwt_token

            return None, "cannot get the token"
        except Exception as e:
            return None, f"{e}"

    def get_user_details(self, user_data):
        user_details = dict()

        user_details["name"] = user_data.get("name")
        user_details["username"] = user_data.get("username")
        user_details["bio"] = user_data.get("bio")
        user_details["age"] = user_data.get("age")

        return user_details

    def get_user_details_by_username(self, username):
        if not username:
            return None, "Please provide username"
        try:
            user = UserDetails.objects.get(username=username)
            return user, None
        except UserDetails.DoesNotExist as exc:
            return None, f'{exc}'
        except Exception as e:
            return None, f'{e}'