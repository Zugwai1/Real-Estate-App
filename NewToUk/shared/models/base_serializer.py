from rest_framework import serializers


class AppBaseSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=5000, required=False)
    status = serializers.BooleanField(required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
