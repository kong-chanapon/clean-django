from app.core.domain.entities.category import Category
from uuid import UUID
from typing import List

class CategoryRepository:
    __category_manager = Category.objects

    @classmethod
    def get_by_id(cls, id: UUID) -> Category:
        return cls.__category_manager.get(pk=id)

    @classmethod
    def get_all(cls) -> List[Category]:
        return list(cls.__category_manager.all())

    @classmethod
    def get_by_url_handle(cls, url_handle: str) -> Category:
        return cls.__category_manager.filter(url_handle=url_handle).first()

    @classmethod
    def create(cls, data: Category) -> Category:
        data.save()
        return data

    @classmethod
    def update(cls, data: Category) -> Category:
        data.save()
        return data

    @classmethod
    def delete(cls, id: UUID) -> Category:
        category = cls.__category_manager.get(pk=id)
        category.delete()
        return category

    @classmethod
    def get_count(cls) -> int:
        return cls.__category_manager.count()

