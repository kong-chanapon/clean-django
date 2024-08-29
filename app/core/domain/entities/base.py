from django.db import models
from django.utils import timezone
from django.contrib import admin

import uuid

class BaseEntity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    class Meta:
        abstract=True

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.created_at = self.created_at or timezone.now()
        self.updated_at = timezone.now()
        return super(BaseEntity, self).save(*args, **kwargs)

class BaseAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'updated_at')
    search_fields = ['pk']