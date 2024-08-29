from .base import BaseEntity, BaseAdmin
from django.db import models
from django.contrib import admin

class BlogImage(BaseEntity):
    file_name = models.CharField(max_length=255, null=False, blank=False)
    file_extension = models.CharField(max_length=255, null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    url = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
            verbose_name = "Blog Image"
            verbose_name_plural = "Blog Images"

    def __str__(self) -> str:
        return f"{self.file_name}"

class BlogImageAdmin(BaseAdmin):
    pass

admin.site.register(BlogImage, BlogImageAdmin)