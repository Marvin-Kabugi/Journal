from rest_framework import serializers

from customuser.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name','username']

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if data['username'] is None:
            data.pop('username')
            return data
        return data