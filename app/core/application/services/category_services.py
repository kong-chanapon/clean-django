from app.infrastructure.repositories.category_repository import CategoryRepository
from app.core.application.dtos.category_dtos import CategoryResponseDto, CreateCategoryRequestDto, UpdateCategoryRequestDto
from app.core.domain.entities.category import Category
from uuid import UUID
from typing import List

from rest_framework.exceptions import NotFound

class CategoryService:
    __repository = CategoryRepository

    @classmethod
    def get_by_id(cls, id: UUID):
        try:
            result = cls.__repository.get_by_id(id)
            return CategoryResponseDto(result).data
        except Category.DoesNotExist:
            raise NotFound("Category not found")
        
    @classmethod
    def get_by_url_handle(cls, url_handle: str):
        try:
            result = cls.__repository.get_by_url_handle(url_handle)
            return CategoryResponseDto(result).data
        except Category.DoesNotExist:
            raise NotFound("Category not found")
        
    @classmethod
    def get_count(cls):
        return cls.__repository.get_count()

    @classmethod
    def get_all(cls):
        result = cls.__repository.get_all()
        return CategoryResponseDto(result, many=True).data

    @classmethod
    def create(cls, data):
        serializer = CreateCategoryRequestDto(data=data)
        if serializer.is_valid(raise_exception=True):
            category = Category(**serializer.validated_data)
            result = cls.__repository.create(category)
            return CategoryResponseDto(result).data

    @classmethod
    def update(cls, id: UUID, update_data: dict):
        serializer = UpdateCategoryRequestDto(data=update_data)
        if serializer.is_valid(raise_exception=True):
            try:
                category = cls.__repository.get_by_id(id)
                validated_data = serializer.validated_data
                category.name = validated_data['name']
                category.url_handle = validated_data['url_handle']
                result = cls.__repository.update(category)
                return CategoryResponseDto(result).data
            except Category.DoesNotExist:
                raise NotFound("Category not found")

    @classmethod
    def delete(cls, id: UUID):
        try:
            result = cls.__repository.get_by_id(id)
            cls.__repository.delete(id)
            return CategoryResponseDto(result).data
        except Category.DoesNotExist:
            raise NotFound("Category not found")
