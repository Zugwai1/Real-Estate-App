from NewToUk.shared.models.base_serializer import AppBaseSerializer
from rest_framework import serializers

from auth_app.serializers.address_serializer import AddressSerializer


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=20, required=False)
    middle_name = serializers.CharField(max_length=20, required=False)
    last_name = serializers.CharField(max_length=20, required=False)
    email = serializers.EmailField(required=False)
    phone_number = serializers.CharField(max_length=20, required=False)
    password = serializers.CharField(read_only=True, max_length=100, required=False)
    username = serializers.CharField(max_length=20, required=False)
    nationality = serializers.CharField(max_length=50, required=False)
    DOB = serializers.DateField(required=False)
    address = AddressSerializer(read_only=True, required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class GetUserSerializer(AppBaseSerializer):
    user = UserSerializer(many=False)


class ListUserSerializer(AppBaseSerializer):
    users = UserSerializer(many=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
