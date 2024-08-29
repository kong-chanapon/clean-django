from rest_framework import serializers

class BlogImageResponseDto(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    file_name = serializers.CharField(max_length=255)
    file_extension = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
    url = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()