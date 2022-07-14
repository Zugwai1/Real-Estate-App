from rest_framework import serializers

from NewToUk.shared.models.base_serializer import AppBaseSerializer
from auth_app.serializers.address_serializer import AddressSerializer
from auth_app.serializers.use_serializer import UserSerializer


class PropertySerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=False)
    type = serializers.CharField(required=False)
    user = UserSerializer(required=False, many=False)
    address = AddressSerializer(many=False, required=False)
    description = serializers.CharField(required=False)
    images = serializers.ListField(child=serializers.CharField(required=False))

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class CreatePropertySerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    type = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    number_line = serializers.IntegerField(required=False)
    street = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    postal_code = serializers.IntegerField(required=False)
    image1 = serializers.FileField(required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class EditPropertySerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    type = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    number_line = serializers.IntegerField(required=False)
    street = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    postal_code = serializers.IntegerField(required=False)
    image1 = serializers.FileField(required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class GetPropertySerializer(AppBaseSerializer):
    property = PropertySerializer(many=False)


class ListPropertySerializer(AppBaseSerializer):
    properties = PropertySerializer(many=True)


class CreatePropertyResponseSerializer(AppBaseSerializer):
    property_id = serializers.UUIDField(required=False)


class EditPropertyResponseSerializer(AppBaseSerializer):
    property_id = serializers.UUIDField(required=False)
