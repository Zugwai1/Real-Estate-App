from NewToUk.shared.models.base_serializer import AppBaseSerializer
from rest_framework import serializers

from auth_app.serializers.address_serializer import AddressSerializer


class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
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


class CreateUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=20, required=True)
    middle_name = serializers.CharField(max_length=20, required=True)
    last_name = serializers.CharField(max_length=20, required=True)
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(max_length=20, required=True)
    password = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(max_length=20, required=True)
    nationality = serializers.CharField(max_length=50, required=True)
    dob = serializers.DateField(required=True)
    number_line = serializers.IntegerField(required=False)
    street = serializers.CharField(required=False)
    city = serializers.CharField(required=True)
    state = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    postal_code = serializers.IntegerField(required=False)
    groups = serializers.CharField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class EditUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=20, required=False)
    middle_name = serializers.CharField(max_length=20, required=False)
    last_name = serializers.CharField(max_length=20, required=False)
    email = serializers.EmailField(required=False)
    phone_number = serializers.CharField(max_length=20, required=False)
    username = serializers.CharField(max_length=20, required=False)
    nationality = serializers.CharField(max_length=50, required=False)
    dob = serializers.DateField(required=False)
    number_line = serializers.IntegerField(required=False)
    street = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    postal_code = serializers.IntegerField(required=False)
    groups = serializers.CharField(required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class GetUserSerializer(AppBaseSerializer):
    user = UserSerializer(many=False)


class ListUserSerializer(AppBaseSerializer):
    users = UserSerializer(many=True)


class ResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    full_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    roles = serializers.ListField(required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UserResponseSerializer(AppBaseSerializer):
    user_id = serializers.UUIDField(required=False)


class LoginResponseSerializer(AppBaseSerializer):
    token = serializers.CharField(required=True)
    user = ResponseSerializer(many=False)


class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
