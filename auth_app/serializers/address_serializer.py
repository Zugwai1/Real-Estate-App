from rest_framework import serializers

from NewToUk.shared.models.BaseSerializer import AppBaseSerializer


class AddressSerializer(AppBaseSerializer):
    number_line = serializers.IntegerField(required=False)
    street = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    postal_code = serializers.IntegerField(required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
