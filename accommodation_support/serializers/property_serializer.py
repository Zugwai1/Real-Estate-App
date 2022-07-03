from rest_framework import serializers

from NewToUk.shared.models.base_serializer import AppBaseSerializer
from auth_app.serializers.address_serializer import AddressSerializer
from auth_app.serializers.use_serializer import UserSerializer


class PropertySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=1000, null=True)
    type = serializers.CharField(max_length=50)
    user = UserSerializer(many=False, read_only=True)
    address = AddressSerializer(many=False, read_only=True)
    description = serializers.CharField(null=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class GetPropertySerializer(AppBaseSerializer):
    property = PropertySerializer(many=False)


class ListPropertySerializer(AppBaseSerializer):
    properties = PropertySerializer(many=True)
