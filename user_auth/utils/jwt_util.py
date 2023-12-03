import jwt
from django.conf import settings
from datetime import datetime, timedelta

from user_auth.constants.constants import Constants


class Auth:
    def generate_jwt_token(self, payload):
        if not payload:
            return None
        try:
            expiration_time = datetime.utcnow() + timedelta(hours=1)

            payload['exp'] = expiration_time
            payload['iat'] = datetime.utcnow()
            encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        except:
            return None
        return encoded_jwt

    def authorize(self, token):
        try:
            decoded_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return decoded_payload, None
        except jwt.ExpiredSignatureError as j:
            return None, Constants.UserConstants.UNAUTHORIZED
        except Exception as e:
            return None, Constants.UserConstants.UNAUTHORIZED
