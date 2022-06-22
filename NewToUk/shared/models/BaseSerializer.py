from rest_framework import serializers


class AppBaseSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
