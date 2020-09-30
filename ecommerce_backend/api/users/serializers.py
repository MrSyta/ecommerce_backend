from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'groups', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user
