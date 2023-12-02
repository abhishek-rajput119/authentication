import jwt
from django.conf import settings
from datetime import datetime,timedelta

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

    def authorize_request(self, token):
        try:
            decoded_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return decoded_payload, None
        except jwt.ExpiredSignatureError as j:
            result = {
                'message': 'token expired',
                'error': f'{j}'
            }
            return False, result
        except Exception as e:
            result = {
                'error': f'{e}'
            }
            return False, result
