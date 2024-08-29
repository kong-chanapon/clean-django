from .base import BaseEntity, BaseAdmin
from django.db import models
from django.contrib import admin

class Category(BaseEntity):
    name = models.CharField(max_length=255, null=False, blank=False)
    url_handle = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
            verbose_name = "Category"
            verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"{self.name}"
    
class CategoryAdmin(BaseAdmin):
    pass

admin.site.register(Category, CategoryAdmin)