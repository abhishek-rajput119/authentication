from rest_framework.serializers import ModelSerializer
from user_auth.models import UserDetails

class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['name', 'username', 'bio', 'age', 'password']

