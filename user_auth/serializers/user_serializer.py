from rest_framework.serializers import ModelSerializer
from user_auth.models import UserDetails

class UserSerializer(ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['name', 'username', 'bio', 'age', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

