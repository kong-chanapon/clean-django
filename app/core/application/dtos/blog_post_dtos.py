from rest_framework import serializers
from app.core.application.dtos.category_dtos import CategoryResponseDto

class BlogPostResponseDto(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    title = serializers.CharField(max_length=255)
    short_description = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=255)
    featured_image_url = serializers.CharField(max_length=255)
    url_handle = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    is_visible = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    categories = CategoryResponseDto(many=True, read_only=True)

class BaseBlogPostRequestDto(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    short_description = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=255)
    featured_image_url = serializers.CharField(max_length=255)
    url_handle = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    is_visible = serializers.BooleanField()
    category_ids = serializers.ListField()

class CreateBlogPostRequestDto(BaseBlogPostRequestDto):
    pass

class UpdateBlogPostRequestDto(BaseBlogPostRequestDto):
    pass