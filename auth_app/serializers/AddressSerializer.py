from rest_framework import serializers

from NewToUk.shared.models.BaseSerializer import AppBaseSerializer


class AddressSerializer(AppBaseSerializer):
    number_line = serializers.IntegerField()
    street = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    country = serializers.CharField()
    postal_code = serializers.IntegerField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
