from .base import BaseEntity, BaseAdmin
from django.db import models
from .category import Category
from django.contrib import admin

class BlogPost(BaseEntity):
    title = models.CharField(max_length=255, null=False, blank=False)
    short_description = models.CharField(max_length=255, null=False, blank=False)
    content = models.CharField(max_length=255, null=False, blank=False)
    featured_image_url = models.CharField(max_length=255, null=False, blank=False)
    url_handle = models.CharField(max_length=255, null=False, blank=False)
    author = models.CharField(max_length=255, null=False, blank=False)
    is_visible = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)

    class Meta:
            verbose_name = "Blog Post"
            verbose_name_plural = "Blog Posts"

    def __str__(self) -> str:
        return f"{self.title}"

class BlogPostAdmin(BaseAdmin):
    pass

admin.site.register(BlogPost, BlogPostAdmin)