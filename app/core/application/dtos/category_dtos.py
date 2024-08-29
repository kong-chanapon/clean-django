from rest_framework import serializers

class CategoryResponseDto(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)
    url_handle = serializers.CharField(max_length=255)

class BaseCategoryRequestDto(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    url_handle = serializers.CharField(max_length=255)

class CreateCategoryRequestDto(BaseCategoryRequestDto):
    pass

class UpdateCategoryRequestDto(BaseCategoryRequestDto):
    pass

