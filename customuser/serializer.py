from rest_framework.serializers import ModelSerializer

from customuser.models import CustomUser

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']