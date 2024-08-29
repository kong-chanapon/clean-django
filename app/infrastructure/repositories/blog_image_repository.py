from app.core.domain.entities.blog_image import BlogImage
from uuid import UUID
from typing import List


class BlogImageRepository:
    __blog_image_manager = BlogImage.objects

    @classmethod
    def save_image(cls, data: BlogImage):
        data.save()
        return data
    
    @classmethod
    def get_all(cls,) -> List[BlogImage]:
        return list(cls.__blog_image_manager.all())