from app.infrastructure.repositories.blog_image_repository import BlogImageRepository
from app.core.application.dtos.blog_image_dtos import BlogImageResponseDto
from app.core.domain.entities.blog_image import BlogImage
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from uuid import uuid4

class BlogImageService:
    __repository = BlogImageRepository

    @classmethod
    def upload_image(cls, file_name: str, title: str, image_file):

        _, file_extension = os.path.splitext(image_file.name)
        unique_file_name = f"{uuid4()}{file_extension}"
        file_path = default_storage.save(f"{unique_file_name}", ContentFile(image_file.read()))

        url = default_storage.url(file_path)

        result = cls.__repository.save_image(BlogImage(
            file_name=file_name,
            file_extension=file_extension,
            title=title,
            url=url
        ))

        return BlogImageResponseDto(result).data
    
    @classmethod
    def get_all(cls):
        result = cls.__repository.get_all()
        return BlogImageResponseDto(result, many=True).data