from app.core.domain.entities.blog_post import BlogPost
from uuid import UUID
from typing import List

class BlogPostRepository:
    __blog_post_manager = BlogPost.objects

    @classmethod
    def get_by_id(cls, id: UUID) -> BlogPost:
        return cls.__blog_post_manager.get(pk=id)

    @classmethod
    def get_all(cls) -> List[BlogPost]:
        return list(cls.__blog_post_manager.all())

    @classmethod
    def get_by_url_handle(cls, url_handle: str) -> BlogPost:
        return cls.__blog_post_manager.filter(url_handle=url_handle)

    @classmethod
    def create(cls, data: BlogPost) -> BlogPost:
        data.save()
        return data

    @classmethod
    def update(cls, data: BlogPost) -> BlogPost:
        data.save()
        return data

    @classmethod
    def delete(cls, id: UUID) -> BlogPost:
        category = cls.__blog_post_manager.get(pk=id)
        category.delete()
        return category

    @classmethod
    def get_count(cls) -> int:
        return cls.__blog_post_manager.count()