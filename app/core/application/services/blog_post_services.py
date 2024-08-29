from app.infrastructure.repositories.blog_post_repository import BlogPostRepository
from app.core.application.dtos.blog_post_dtos import BlogPostResponseDto, CreateBlogPostRequestDto, UpdateBlogPostRequestDto
from app.core.domain.entities.blog_post import BlogPost
from app.core.domain.entities.category import Category
from uuid import UUID

from rest_framework.exceptions import NotFound

class BlogPostService:
    __repository = BlogPostRepository

    @classmethod
    def get_by_id(cls, id: UUID):
        try:
            result = cls.__repository.get_by_id(id)
            return BlogPostResponseDto(result).data
        except BlogPost.DoesNotExist:
            raise NotFound("Blog post not found")
        
    @classmethod
    def get_by_url_handle(cls, url_handle: str):
        try:
            result = cls.__repository.get_by_url_handle(url_handle)
            return BlogPostResponseDto(result, many=True).data
        except BlogPost.DoesNotExist:
            raise NotFound("Blog post not found")
        
    @classmethod
    def get_count(cls):
        return cls.__repository.get_count()

    @classmethod
    def get_all(cls):
        result = cls.__repository.get_all()
        return BlogPostResponseDto(result, many=True).data

    @classmethod
    def create(cls, data):
        serializer = CreateBlogPostRequestDto(data=data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            category_ids = validated_data.pop('category_ids')
            categories = set(Category.objects.filter(id__in=category_ids))
            blog_post = BlogPost(**validated_data)
            cls.__repository.create(blog_post)

            blog_post.categories.set(categories)
            result = cls.__repository.create(blog_post)
            return BlogPostResponseDto(result).data

    @classmethod
    def update(cls, id: UUID, update_data: dict):
        serializer = UpdateBlogPostRequestDto(data=update_data)
        if serializer.is_valid(raise_exception=True):
            try:
                blog_post = cls.__repository.get_by_id(id)
                blog_post.categories.remove()
                validated_data = serializer.validated_data
                category_ids = validated_data.pop('category_ids')
                categories = Category.objects.filter(id__in=category_ids)
                
                # Update the blog post fields
                blog_post.title = validated_data['title']
                blog_post.short_description = validated_data['short_description']
                blog_post.content = validated_data['content']
                blog_post.author = validated_data['author']
                blog_post.featured_image_url = validated_data['featured_image_url']
                blog_post.url_handle = validated_data['url_handle']
                blog_post.is_visible = validated_data['is_visible']
                blog_post.categories.set(categories)  # Many-to-many field update

                # Save the updated blog post using the repository
                result = cls.__repository.update(blog_post)
                return BlogPostResponseDto(result).data

            except BlogPost.DoesNotExist:
                raise NotFound("Blog post not found")

    @classmethod
    def delete(cls, id: UUID):
        try:
            result = cls.__repository.delete(id)
            result.id = id
            return BlogPostResponseDto(result).data
        except BlogPost.DoesNotExist:
            raise NotFound("Blog post not found")
