from rest_framework import serializers

from customuser.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name','username', 'password']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('password')
        if data['username'] is None:
            data.pop('username')
            return data
        return data
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            validated_data.pop('password')
        
        super().update(instance, validated_data)
            