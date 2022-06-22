from NewToUk.shared.models.BaseSerializer import AppBaseSerializer
from rest_framework import serializers

from auth_app.serializers.AddressSerializer import AddressSerializer


class UserSerializer(AppBaseSerializer):
    first_name = serializers.CharField(max_length=20)
    middle_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=20)
    password = serializers.CharField(read_only=True, max_length=100)
    username = serializers.CharField(max_length=20)
    nationality = serializers.CharField(max_length=50)
    DOB = serializers.DateField()
    address = AddressSerializer(read_only=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
